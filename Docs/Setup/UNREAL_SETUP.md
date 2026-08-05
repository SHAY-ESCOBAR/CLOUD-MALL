# Unreal Setup

## Status

No `.uproject` exists in this repository yet (by design — see
`Docs/Architecture/UNREAL_STRUCTURE.md`). This document is the procedure for
creating it.

## Creating the project

1. Install Unreal Engine via the Epic Games Launcher (version to be decided
   and recorded here once chosen).
2. Create a new project:
   - Category: Games (or the category appropriate to the target output).
   - Template: Blank.
   - Target platform: Desktop.
   - Quality preset: match target hardware (decide later, record here).
   - Starter content: decide based on whether we want Epic's sample
     assets mixed in (default recommendation: **off**, to keep
     `Content/CORE_AI/` clean of unrelated starter assets).
   - Project location: this repository's root, so the `.uproject` sits next
     to `Content/`, `Config/`, etc.
   - Project name: `CLOUD-MALL` (or as decided at creation time).
3. After creation, confirm Unreal's own `Content/` folder browser shows the
   `CORE_AI` subfolder structure from `Docs/Architecture/UNREAL_STRUCTURE.md`
   — recreate any subfolders Unreal didn't pick up (git doesn't track empty
   folders).
4. Commit the new `.uproject`, `Config/`, and any generated `Source/` files
   on a feature branch (never `main`).

## Required plugins (to be finalized)

- Editor Scripting Utilities (built-in Unreal plugin) — enables Python/BP
  editor automation.
- Unreal MCP bridge — see `Docs/Architecture/MCP_ARCHITECTURE.md` (specific
  plugin TBD).

Do not enable unfamiliar/unverified third-party plugins without review.

## Verifying the project

- Open the `.uproject`, confirm the Editor loads without errors.
- Confirm Play In Editor works on the default/empty map.
- Run `Scripts/Validation/validate-repository.ps1`.
