# CLI Design & Architecture

Best practices for building internal scripts that don't break.

## Core Tenets

1. **Deterministic Execution**
   - The CLI should do the exact same thing if run twice, or gracefully warn the user ("Files already processed").
   
2. **Help Documentation**
   - No undocumented tools. If it takes arguments, it must respond to `-h` or `--help`.

3. **Safe by Default**
   - Any script that interacts with external APIs or deletes files should require an explicit `--confirm` flag or default to `--dry-run` behavior.

4. **Modular Logic**
   - Do not write massive 500-line procedural scripts. Extract the core logic into testable functions, and only use the CLI layer to parse arguments and print status.
