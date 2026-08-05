# Unreal Setup

## Status

No `.uproject` exists in this repository yet (by design — see
`Docs/Architecture/UNREAL_STRUCTURE.md`). This document is the procedure for
creating it.

## Confirmed local environment

- **Unreal Engine version:** 5.8
- **Local clone path:** `C:\Users\ANUBiS\Documents\CLOUD-MALL`
- **OS:** Windows

⚠️ **Do not clone or create the project under `C:\Windows\system32` or any
other protected system folder.** Windows Controlled Folder Access blocks
git/file operations there in ways that are hard to diagnose (silent partial
failures on `Move-Item`, `git clean`, etc.), even when PowerShell is
running elevated. Always work under a normal user folder such as
`Documents` or a dedicated `C:\Dev\` folder. If PowerShell opens directly
into `system32`, `cd` to `$env:USERPROFILE\Documents` (or wherever you keep
projects) before running any git commands.

## Creating the project

1. Install Unreal Engine via the Epic Games Launcher — **5.8**, already
   installed.
2. Create a new project:
   - Category: Games (or the category appropriate to the target output).
   - **Template: Blank** (not "Intro To Unreal" — that pulls in Epic's
     tutorial content/assets we don't want).
   - Target platform: Desktop.
   - Quality preset: match target hardware (decide later, record here).
   - Starter content: **off**, to keep `Content/CORE_AI/` clean of
     unrelated starter assets.
   - Project location: `C:\Users\ANUBiS\Documents\CLOUD-MALL` (this
     repository's clone), so the `.uproject` sits next to `Content/`,
     `Config/`, etc.
   - Project name: `CLOUD-MALL`.
3. After creation, confirm Unreal's own `Content/` folder browser shows the
   `CORE_AI` subfolder structure from `Docs/Architecture/UNREAL_STRUCTURE.md`
   — recreate any subfolders Unreal didn't pick up (git doesn't track empty
   folders; this repo currently holds them with `.gitkeep` files).
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
