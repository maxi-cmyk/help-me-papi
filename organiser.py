#!/usr/bin/env python3

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


PATH_TAG_RE = re.compile(r"(?<!\w)#([A-Za-z][A-Za-z0-9_-]*(?:/[A-Za-z0-9_-]+)+)")
CONTENT_FOLDERS = {"skills", "resources", "ideas", "prompts"}
DEFAULT_ROOT = Path(".")
DEFAULT_SOURCE = Path("inbox.md")


def normalize_segment(segment: str) -> str:
    return segment.strip().lower().replace("_", "-")


def normalize_path_tag(tag: str) -> str:
    parts = [normalize_segment(part) for part in tag.strip().strip("/").split("/") if part]
    return "/".join(parts)


def split_blocks(text: str) -> list[str]:
    chunks = re.split(r"\n\s*\n", text.strip())
    return [chunk.strip() for chunk in chunks if chunk.strip()]


def build_target_maps(root: Path) -> tuple[dict[str, Path], dict[str, Path]]:
    exact_targets: dict[str, Path] = {}
    shorthand_candidates: dict[str, list[Path]] = {}

    for path in sorted(root.rglob("*.md")):
        if ".git" in path.parts:
            continue
        if path.name.lower() in {"readme.md", "inbox.md"}:
            continue
        relative = path.relative_to(root)
        parts = list(relative.parts)
        parts[-1] = Path(parts[-1]).stem
        exact_tag = normalize_path_tag("/".join(parts))
        exact_targets.setdefault(exact_tag, path)

        if len(parts) >= 3 and normalize_segment(parts[-2]) in CONTENT_FOLDERS:
            shorthand_parts = parts[:-2] + [parts[-1]]
            shorthand_tag = normalize_path_tag("/".join(shorthand_parts))
            shorthand_candidates.setdefault(shorthand_tag, []).append(path)

    shorthand_targets = {
        tag: paths[0]
        for tag, paths in shorthand_candidates.items()
        if len({candidate.as_posix() for candidate in paths}) == 1
    }

    return exact_targets, shorthand_targets


def resolve_destination(
    block: str, exact_targets: dict[str, Path], shorthand_targets: dict[str, Path]
) -> tuple[Path | None, list[str]]:
    tags = [normalize_path_tag(match.group(1)) for match in PATH_TAG_RE.finditer(block)]
    if not tags:
        return None, []

    for tag in tags:
        if tag in exact_targets:
            return exact_targets[tag], tags

    for tag in tags:
        if tag in shorthand_targets:
            return shorthand_targets[tag], tags

    return None, tags


def append_block(destination: Path, block: str, dry_run: bool) -> None:
    block = block.strip()
    if not block:
        return

    destination.parent.mkdir(parents=True, exist_ok=True)

    if dry_run:
        return

    existing = destination.read_text(encoding="utf-8") if destination.exists() else ""
    if block in existing:
        return

    if existing.strip():
        new_text = existing.rstrip() + "\n\n" + block + "\n"
    else:
        new_text = block + "\n"

    destination.write_text(new_text, encoding="utf-8")


def rewrite_source(source: Path, remaining_blocks: list[str], dry_run: bool) -> None:
    if dry_run:
        return

    if not remaining_blocks:
        source.write_text("", encoding="utf-8")
        return

    source.write_text("\n\n".join(remaining_blocks).rstrip() + "\n", encoding="utf-8")


def organise(source: Path, root: Path, dry_run: bool) -> int:
    if not root.exists():
        print(f"error: root folder not found: {root}", file=sys.stderr)
        return 1

    if not source.exists():
        print(f"error: source file not found: {source}", file=sys.stderr)
        return 1

    exact_targets, shorthand_targets = build_target_maps(root)
    blocks = split_blocks(source.read_text(encoding="utf-8"))

    moved_count = 0
    skipped_count = 0
    remaining_blocks: list[str] = []

    for block in blocks:
        destination, tags = resolve_destination(block, exact_targets, shorthand_targets)

        if destination is None:
            remaining_blocks.append(block)
            if tags:
                skipped_count += 1
            continue

        append_block(destination, block, dry_run)
        moved_count += 1
        print(f"{source} -> {destination} [{', '.join(tags)}]")

    rewrite_source(source, remaining_blocks, dry_run)
    print(f"moved: {moved_count}")
    print(f"unmatched tagged blocks left in source: {skipped_count}")
    print(f"remaining blocks in source: {len(remaining_blocks)}")
    return 0


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
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    return organise(Path(args.source), Path(args.root), args.dry_run)


if __name__ == "__main__":
    raise SystemExit(main())
