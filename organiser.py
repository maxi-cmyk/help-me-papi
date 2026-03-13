#!/usr/bin/env python3

from __future__ import annotations

import argparse
import hashlib
import re
import shutil
import sys
from pathlib import Path


# ---------------------------------------------------------------------------
# Constants & configuration
# ---------------------------------------------------------------------------

PATH_TAG_RE = re.compile(r"(?<!\w)#([A-Za-z][A-Za-z0-9_-]*(?:/[A-Za-z0-9_-]+)+)")
FENCED_BLOCK_RE = re.compile(r"```.*?```|`[^`\n]+`", re.DOTALL)
CONTRIBUTOR_RE = re.compile(r"<!--\s*@([^>]+?)\s*-->")

DEFAULT_CONTENT_FOLDERS = {"skills", "ideas"}
CONTENT_FOLDERS_FILE = ".content-folders"
CATALOG_FILE = "catalog.md"
FOLDER_INBOX = "_inbox.md"

DEFAULT_ROOT = Path(".")
DEFAULT_SOURCE = Path("inbox.md")


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def load_content_folders(root: Path) -> set[str]:
    """Load content folder names from config file, falling back to defaults."""
    config = root / CONTENT_FOLDERS_FILE
    if config.exists():
        names = {
            line.strip().lower()
            for line in config.read_text(encoding="utf-8").splitlines()
            if line.strip() and not line.strip().startswith("#")
        }
        if names:
            return names
    return DEFAULT_CONTENT_FOLDERS.copy()


def normalize_segment(segment: str) -> str:
    return segment.strip().lower().replace("_", "-")


def normalize_path_tag(tag: str) -> str:
    parts = [normalize_segment(part) for part in tag.strip().strip("/").split("/") if part]
    return "/".join(parts)


def normalize_block(block: str) -> str:
    """Collapse whitespace for reliable comparison."""
    return " ".join(block.split()).strip()


def block_hash(block: str) -> str:
    """Produce a short hash of a normalised block for dedup."""
    return hashlib.sha256(normalize_block(block).encode("utf-8")).hexdigest()[:16]


def strip_code_spans(text: str) -> str:
    """Remove fenced code blocks and inline code so tags inside them are ignored."""
    return FENCED_BLOCK_RE.sub("", text)


def split_blocks(text: str) -> list[str]:
    chunks = re.split(r"\n\s*\n", text.strip())
    return [chunk.strip() for chunk in chunks if chunk.strip()]


def resolve_folder_case_insensitive(root: Path, segments: list[str]) -> Path | None:
    """Walk down from root matching each segment case-insensitively.

    Returns the real path if every segment matches a directory, else None.
    e.g. segments=["ai", "skills"] matches root/AI/skills/
    """
    current = root
    for seg in segments:
        match = None
        try:
            for child in current.iterdir():
                if child.is_dir() and child.name.lower() == seg.lower():
                    match = child
                    break
        except OSError:
            return None
        if match is None:
            return None
        current = match
    return current


# ---------------------------------------------------------------------------
# Target map building
# ---------------------------------------------------------------------------


def build_target_maps(
    root: Path, content_folders: set[str]
) -> tuple[dict[str, Path], dict[str, Path]]:
    exact_targets: dict[str, Path] = {}
    shorthand_candidates: dict[str, list[Path]] = {}

    for path in sorted(root.rglob("*.md")):
        if ".git" in path.parts:
            continue
        if path.name.lower() in {"readme.md", "inbox.md", FOLDER_INBOX.lower(), CATALOG_FILE.lower()}:
            continue

        relative = path.relative_to(root)
        parts = list(relative.parts)
        parts[-1] = Path(parts[-1]).stem
        exact_tag = normalize_path_tag("/".join(parts))
        exact_targets.setdefault(exact_tag, path)

        # Build shorthand that skips the content-type folder
        # e.g. backend/skills/auth -> backend/auth
        if len(parts) >= 3 and normalize_segment(parts[-2]) in content_folders:
            shorthand_parts = parts[:-2] + [parts[-1]]
            shorthand_tag = normalize_path_tag("/".join(shorthand_parts))
            shorthand_candidates.setdefault(shorthand_tag, []).append(path)

    shorthand_targets: dict[str, Path] = {}
    ambiguous_tags: dict[str, list[Path]] = {}

    for tag, paths in shorthand_candidates.items():
        unique = list({p.as_posix(): p for p in paths}.values())
        if len(unique) == 1:
            shorthand_targets[tag] = unique[0]
        else:
            ambiguous_tags[tag] = unique

    return exact_targets, shorthand_targets, ambiguous_tags  # type: ignore[return-value]


# ---------------------------------------------------------------------------
# Tag extraction (code-aware)
# ---------------------------------------------------------------------------


def extract_tags(block: str) -> list[str]:
    """Extract path tags from a block, ignoring anything inside code spans/fences."""
    cleaned = strip_code_spans(block)
    return [normalize_path_tag(m.group(1)) for m in PATH_TAG_RE.finditer(cleaned)]


# ---------------------------------------------------------------------------
# Resolution
# ---------------------------------------------------------------------------


def resolve_destination(
    block: str,
    exact_targets: dict[str, Path],
    shorthand_targets: dict[str, Path],
    ambiguous_tags: dict[str, list[Path]],
    create: bool,
    root: Path,
    content_folders: set[str],
) -> tuple[Path | None, list[str], str | None]:
    """Resolve a block's tags to a destination file.

    Returns (destination_path, tags_found, warning_or_none).
    """
    tags = extract_tags(block)
    if not tags:
        return None, [], None

    # Pass 1: exact match
    for tag in tags:
        if tag in exact_targets:
            return exact_targets[tag], tags, None

    # Pass 2: shorthand match
    for tag in tags:
        if tag in shorthand_targets:
            return shorthand_targets[tag], tags, None

    # Pass 3: check for ambiguity and report it
    for tag in tags:
        if tag in ambiguous_tags:
            candidates = ambiguous_tags[tag]
            paths_str = ", ".join(str(p) for p in candidates)
            warning = f"ambiguous tag #{tag} — matches: {paths_str}"
            return None, tags, warning

    # Pass 4: folder-level tag (e.g. #frontend/skills -> frontend/skills/_inbox.md)
    for tag in tags:
        folder = resolve_folder_case_insensitive(root, tag.split("/"))
        if folder is not None and folder.is_dir():
            dest = folder / FOLDER_INBOX
            return dest, tags, None

    # Pass 5: auto-create if --create is set
    if create:
        tag = tags[0]
        parts = tag.split("/")

        # If the last segment is a content-type folder name, create the directory
        # e.g. #backend/resources -> create backend/resources/_inbox.md
        if parts[-1] in content_folders:
            folder = _resolve_or_create_path(root, parts)
            dest = folder / FOLDER_INBOX
            return dest, tags, None

        # Otherwise create a file
        dest = infer_create_path(tag, root, content_folders)
        if dest is not None:
            exact_targets[tag] = dest  # register for future blocks
            return dest, tags, None

    return None, tags, None


def infer_create_path(tag: str, root: Path, content_folders: set[str]) -> Path | None:
    """Turn a tag into a file path, inferring content-type folder when possible.

    Uses existing directory casing when available to avoid creating duplicate
    folders on case-sensitive filesystems (e.g. ai/ alongside AI/).

    #backend/auth           -> backend/skills/auth.md   (defaults to skills/)
    #backend/skills/auth    -> backend/skills/auth.md   (explicit)
    #frontend/ideas/ui      -> frontend/ideas/ui.md     (explicit)
    """
    parts = tag.split("/")
    if len(parts) < 2:
        return None

    # If the second-to-last segment is already a content folder, use as-is
    if len(parts) >= 3 and parts[-2] in content_folders:
        base = _resolve_or_create_path(root, parts[:-1])
        return base / f"{parts[-1]}.md"

    # Otherwise, default to skills/ as the content-type folder
    domain_parts = parts[:-1]
    topic = parts[-1]
    base = _resolve_or_create_path(root, domain_parts + ["skills"])
    return base / f"{topic}.md"


def _resolve_or_create_path(root: Path, segments: list[str]) -> Path:
    """Resolve segments against existing dirs (case-insensitive), falling back to literal names.

    For each segment, if a matching directory already exists, use its real name.
    Otherwise use the segment as-is (which will be lowercase from normalization).
    """
    current = root
    for seg in segments:
        match = None
        if current.is_dir():
            for child in current.iterdir():
                if child.is_dir() and child.name.lower() == seg.lower():
                    match = child
                    break
        if match is not None:
            current = match
        else:
            current = current / seg
    return current


# ---------------------------------------------------------------------------
# File I/O
# ---------------------------------------------------------------------------


def existing_block_hashes(path: Path) -> set[str]:
    """Get hashes of all blocks already in a file for dedup."""
    if not path.exists():
        return set()
    text = path.read_text(encoding="utf-8")
    return {block_hash(b) for b in split_blocks(text)}


def append_block(destination: Path, block: str, dry_run: bool) -> bool:
    """Append a block to a file. Returns False if it was a duplicate."""
    block = block.strip()
    if not block:
        return False

    destination.parent.mkdir(parents=True, exist_ok=True)

    hashes = existing_block_hashes(destination)
    if block_hash(block) in hashes:
        return False

    if dry_run:
        return True

    existing = destination.read_text(encoding="utf-8") if destination.exists() else ""

    if existing.strip():
        new_text = existing.rstrip() + "\n\n" + block + "\n"
    else:
        new_text = block + "\n"

    destination.write_text(new_text, encoding="utf-8")
    return True


def backup_file(path: Path) -> Path:
    """Create a .bak copy of the file before modifying it."""
    backup = path.with_suffix(path.suffix + ".bak")
    shutil.copy2(path, backup)
    return backup


def rewrite_source(source: Path, remaining_blocks: list[str], dry_run: bool) -> None:
    if dry_run:
        return

    if not remaining_blocks:
        source.write_text("", encoding="utf-8")
        return

    source.write_text("\n\n".join(remaining_blocks).rstrip() + "\n", encoding="utf-8")


# ---------------------------------------------------------------------------
# Main orchestration
# ---------------------------------------------------------------------------


def organise(source: Path, root: Path, dry_run: bool, create: bool) -> int:
    if not root.exists():
        print(f"error: root folder not found: {root}", file=sys.stderr)
        return 1

    if not source.exists():
        print(f"error: source file not found: {source}", file=sys.stderr)
        return 1

    content_folders = load_content_folders(root)
    exact_targets, shorthand_targets, ambiguous_tags = build_target_maps(root, content_folders)
    blocks = split_blocks(source.read_text(encoding="utf-8"))

    moved_count = 0
    duplicate_count = 0
    skipped_count = 0
    untagged_count = 0
    created_count = 0
    warnings: list[str] = []
    remaining_blocks: list[str] = []

    for block in blocks:
        destination, tags, warning = resolve_destination(
            block, exact_targets, shorthand_targets, ambiguous_tags, create, root, content_folders
        )

        if warning:
            warnings.append(warning)

        if destination is None:
            remaining_blocks.append(block)
            if tags:
                skipped_count += 1
            else:
                untagged_count += 1
            continue

        # Track auto-created files
        if not destination.exists():
            created_count += 1

        was_new = append_block(destination, block, dry_run)
        if was_new:
            moved_count += 1
            tag_str = ", ".join(tags)
            prefix = "[dry-run] " if dry_run else ""
            print(f"{prefix}{source} -> {destination} [{tag_str}]")
        else:
            duplicate_count += 1
            remaining_blocks.append(block)

    # Backup before rewriting source
    if not dry_run and (moved_count > 0 or duplicate_count > 0):
        bak = backup_file(source)
        print(f"backup: {bak}")

    rewrite_source(source, remaining_blocks, dry_run)

    # Summary
    print(f"\n--- summary ---")
    print(f"moved:      {moved_count}")
    if created_count:
        print(f"created:    {created_count} new file(s)")
    if duplicate_count:
        print(f"duplicates: {duplicate_count} (kept in source)")
    print(f"untagged:   {untagged_count}")
    print(f"unmatched:  {skipped_count}")
    print(f"remaining:  {len(remaining_blocks)}")

    if warnings:
        print(f"\n--- warnings ---")
        for w in warnings:
            print(f"  ⚠ {w}")

    return 0


# ---------------------------------------------------------------------------
# Catalog generation
# ---------------------------------------------------------------------------


def extract_contributors(path: Path) -> list[str]:
    """Extract contributor names from <!-- @name, @name --> comment at top of file."""
    try:
        text = path.read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError):
        return []

    # Check the first 5 lines for a contributor comment
    for line in text.splitlines()[:5]:
        match = CONTRIBUTOR_RE.search(line)
        if match:
            raw = match.group(1)
            return [
                name.strip().lstrip("@")
                for name in raw.split(",")
                if name.strip()
            ]
    return []


def extract_title(path: Path) -> str | None:
    """Extract the first heading from a markdown file, if any."""
    try:
        text = path.read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError):
        return None

    for line in text.splitlines():
        line = line.strip()
        if line.startswith("# "):
            return line.lstrip("# ").strip()
    return None


def generate_catalog(root: Path) -> int:
    """Scan the repo and generate a catalog.md grouped by domain."""
    if not root.exists():
        print(f"error: root folder not found: {root}", file=sys.stderr)
        return 1

    content_folders = load_content_folders(root)
    skip_names = {"readme.md", "inbox.md", CATALOG_FILE.lower(), FOLDER_INBOX.lower()}

    # Collect files grouped by domain (top-level folder)
    # Structure: { domain: { content_type: [ (relative_path, title, contributors) ] } }
    domains: dict[str, dict[str, list[tuple[Path, str | None, list[str]]]]] = {}
    root_files: list[tuple[Path, str | None, list[str]]] = []

    for path in sorted(root.rglob("*.md")):
        if ".git" in path.parts:
            continue
        if path.name.lower() in skip_names:
            continue

        relative = path.relative_to(root)
        parts = list(relative.parts)

        # Root-level files (like decisions.md)
        if len(parts) == 1:
            root_files.append((relative, extract_title(path), extract_contributors(path)))
            continue

        domain = parts[0]
        title = extract_title(path)
        contributors = extract_contributors(path)

        # Determine content type
        content_type = "other"
        for part in parts[1:]:
            if normalize_segment(part) in content_folders:
                content_type = normalize_segment(part)
                break

        domains.setdefault(domain, {}).setdefault(content_type, []).append(
            (relative, title, contributors)
        )

    # Build the catalog
    lines: list[str] = []
    lines.append("# Catalog")
    lines.append("")
    lines.append("> Auto-generated by `organiser.py --catalog`. Do not edit by hand.")
    lines.append("")

    # Contributor index
    all_contributors: dict[str, list[str]] = {}
    for domain, types in domains.items():
        for entries in types.values():
            for rel_path, _, contribs in entries:
                for c in contribs:
                    all_contributors.setdefault(c, []).append(str(rel_path))

    if all_contributors:
        lines.append("## Contributors")
        lines.append("")
        for name in sorted(all_contributors):
            count = len(all_contributors[name])
            lines.append(f"- **@{name}** — {count} file{'s' if count != 1 else ''}")
        lines.append("")

    # Root-level files
    if root_files:
        lines.append("## Repo-level")
        lines.append("")
        for rel_path, title, contribs in root_files:
            lines.append(_format_catalog_entry(rel_path, title, contribs))
        lines.append("")

    # Content type display order
    type_order = ["skills", "ideas", "other"]

    for domain in sorted(domains):
        lines.append(f"## {domain}")
        lines.append("")

        types = domains[domain]
        sorted_types = sorted(types.keys(), key=lambda t: type_order.index(t) if t in type_order else 99)

        for content_type in sorted_types:
            entries = types[content_type]
            label = content_type.title() if content_type != "other" else "Other"
            lines.append(f"### {label}")
            lines.append("")
            for rel_path, title, contribs in entries:
                lines.append(_format_catalog_entry(rel_path, title, contribs))
            lines.append("")

    catalog_path = root / CATALOG_FILE
    catalog_path.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")
    print(f"catalog: {catalog_path}")

    # Stats
    total_files = sum(
        len(entries) for types in domains.values() for entries in types.values()
    ) + len(root_files)
    print(f"  {len(domains)} domain(s), {total_files} file(s), {len(all_contributors)} contributor(s)")

    return 0


def _format_catalog_entry(rel_path: Path, title: str | None, contribs: list[str]) -> str:
    """Format a single catalog line."""
    display = title if title else rel_path.stem.replace("-", " ").title()
    contrib_str = f"  ({'@' + ', @'.join(contribs)})" if contribs else ""
    return f"- [{display}]({rel_path}){contrib_str}"


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Organise markdown blocks into repo files using #path-style tags."
    )
    parser.add_argument(
        "source",
        nargs="?",
        default=str(DEFAULT_SOURCE),
        help="Markdown file to scan for tagged blocks. Defaults to inbox.md.",
    )
    parser.add_argument(
        "--root",
        default=str(DEFAULT_ROOT),
        help="Repo root used to resolve tags into markdown files. Defaults to the current directory.",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Print the moves without modifying any files.",
    )
    parser.add_argument(
        "--create",
        action="store_true",
        help="Auto-create missing target files from tag paths. "
        "Shorthand tags (e.g. #backend/auth) default to the skills/ subfolder.",
    )
    parser.add_argument(
        "--catalog",
        action="store_true",
        help="Generate catalog.md from all files in the repo, then exit. "
        "Skips the normal inbox sorting.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    root = Path(args.root)

    if args.catalog:
        return generate_catalog(root)

    return organise(Path(args.source), root, args.dry_run, args.create)


if __name__ == "__main__":
    raise SystemExit(main())