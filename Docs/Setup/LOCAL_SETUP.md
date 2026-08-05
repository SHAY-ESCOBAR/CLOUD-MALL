# Local Setup

## Prerequisites

- Git
- Git LFS
- GitHub CLI (`gh`), authenticated (`gh auth status`)
- Unreal Engine (version TBD once installed — record it here)
- Claude Code

Run `Scripts/Setup/setup-project.ps1` (Windows PowerShell) to check all of
the above without installing or changing anything.

## Steps

1. Clone this repository.
2. `git lfs install` then `git lfs pull`.
3. Run `Scripts/Setup/setup-project.ps1` and resolve anything reported
   missing.
4. Create/open the Unreal project per `Docs/Setup/UNREAL_SETUP.md`.
5. Install Claude Code and run it from the repository root.
6. Follow `Docs/Architecture/MCP_ARCHITECTURE.md` to connect MCP once
   available.
7. Run `Scripts/Validation/validate-repository.ps1` before your first
   commit.
