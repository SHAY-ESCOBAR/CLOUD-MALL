# Unreal Project Structure

## Status

No `.uproject` exists yet. This document describes how the repository's
folders map onto a real Unreal project once one is created (Phase 2 of
`ROADMAP.md`), and the conventions to follow from that point on.

## Folder mapping

| Repo folder | Unreal meaning |
|---|---|
| `Config/` | `.ini` files (`DefaultEngine.ini`, `DefaultGame.ini`, etc.) |
| `Content/` | Unreal's `Content/` folder — mounted as `/Game/` in the Editor |
| `Content/CORE_AI/` | All AI-generated / AI-managed content. Never mix hand-authored and generated content in the same folder. |
| `Plugins/` | Engine plugins used by this project (MCP bridge, editor utilities) |
| `Source/` | C++ source, if/when the project needs native code |
| `Saved/`, `Intermediate/`, `Binaries/`, `DerivedDataCache/` | Local-only, engine-generated, gitignored |

## `Content/CORE_AI/` subfolders

- `Blueprints/` — gameplay/logic Blueprints
- `Materials/` — materials and material instances
- `Meshes/` — static/skeletal meshes
- `Textures/` — texture assets
- `Lighting/` — lighting setups/presets
- `Maps/` — levels
- `Sequences/` — Level Sequences / cinematics
- `Widgets/` — UMG widgets (UI)
- `References/` — source reference material (images, sketches, video stills) kept alongside the content they informed
- `Generated/` — intermediate/generated-but-not-final output, reviewed before promotion elsewhere
- `Documentation/` — per-asset documentation (see rule 11 in `CLAUDE.md`)

## Naming conventions

- Descriptive names only — never `NewBlueprint`, `Cube1`, `Material2`.
- Prefix by type where useful (e.g. `BP_`, `M_`, `MI_`, `SM_`, `WBP_`),
  followed by a descriptive name, e.g. `BP_AutomaticDoor_MainEntrance`.

## Scale

1 centimeter = 1 Unreal Unit (Unreal's default). Always model/place at real
world scale.

## Creating the `.uproject` (when ready)

1. Open Unreal Engine, choose **Games > Blank** (or the appropriate
   template), and create the project **inside this repository's root** (or
   in a separate working folder that is then merged into this repo layout —
   decide based on Unreal's own folder requirements at the time).
2. Confirm the Editor's `Content/` folder matches the `Content/CORE_AI/`
   layout above (create the subfolders inside the Editor's Content Browser
   if Unreal didn't pick up the existing empty folders — git does not track
   empty folders, so they may need to be recreated once real content exists,
   or kept with `.gitkeep` files in the meantime).
3. Commit the generated `.uproject`, `Config/`, and any initial `Source/`
   files on a feature branch — never directly to `main`.
