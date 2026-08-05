# MCP Architecture & Unreal Automation Plan (the "Unreal Control Layer")

## Status

Not yet installed. This is the plan to be filled in once an Unreal MCP
server/plugin is chosen and installed locally (Phase 4 of `ROADMAP.md`).

## The core problem this solves

Claude Code can write C++, Blueprints-as-script, JSON, Python, and Editor
Utility scripts — but on its own it cannot actually open the Unreal
Editor and see what happened. This session in particular runs in a remote
Linux cloud environment, not on the local Windows machine where Unreal is
installed — so **there is no direct control today**. Without a bridge,
Claude can prepare everything but never press the buttons.

```
Claude Code
   |
   v
Access to the project folder and a local terminal   <-- must run on the
   |                                                     LOCAL machine,
   v                                                     not this session
Unreal Engine CLI / Python / Automation Tool
   |
   v
Unreal Editor
```

**Rule: never claim an action was performed inside the Editor unless it
actually was.** If there is no local bridge available in a given session,
say so plainly and produce the files/scripts/instructions instead of
pretending.

## What MCP is for here

MCP (Model Context Protocol) is the bridge that lets Claude Code call into
a running Unreal Editor session as a set of tools — e.g. spawn an actor,
create a Blueprint, open a map, take a screenshot — instead of Claude Code
editing `.uasset`/`.umap` binary files directly (which is unsafe and
unsupported).

```
Claude Code  <-- MCP (stdio / local socket) -->  Unreal MCP server/plugin  <-->  Unreal Editor (in-process or companion process)
```

## To be filled in once chosen

- Which MCP server/plugin is used (name, source, license, install method).
- Transport (stdio vs. local HTTP/socket) and how Claude Code's MCP client
  config points at it.
- Full list of exposed tools and what each one does.
- Authentication/authorization model, if any (should stay local-only; no
  exposing the bridge to the public internet).
- Failure modes: what happens if the Editor isn't running, if a call
  targets a locked/checked-out asset, etc.
- How `Scripts/MCP/test-mcp-connection.ps1` verifies the connection.

## Target capabilities of the control layer (Phase 8/9 of `ROADMAP.md`)

Once built, the bridge should support:

- Opening the project.
- Launching the Unreal Editor via command.
- Running Python inside Unreal.
- Creating Actors and Levels.
- Importing assets.
- Reading logs.
- Taking screenshots.
- Running a Build.
- Returning errors back to Claude Code.
- Fix-and-rerun loop.

## Editor automation tool (store creation from template)

A longer-term Editor tool (Editor Utility Widget, Unreal Python,
Blueprints, Data Assets, and/or Commandlets — evaluate which fits best
once building this) that can:

- Create a new store from the Store Template
  (`Docs/Architecture/UNREAL_GAME_ARCHITECTURE.md`).
- Select a store category.
- Auto-generate the storefront.
- Place shelves.
- Place product points.
- Load a Store Configuration (`Docs/Architecture/DATA_MODEL.md`).
- Swap logo and brand colors.
- Generate signage.
- Run error checks.
- Produce a test Build.

This is what eventually makes "add a new store" a data/config operation
instead of a bespoke Unreal build — the core of the "mall-generation
system" product vision in `Docs/PROJECT_VISION.md`.

## Safety constraints for any MCP tool call

- Every MCP-driven change must be inside `Content/CORE_AI/` (or, once the
  Mall Kit folders exist, the appropriate `Content/Mall/*` subfolder after
  promotion — see `Docs/Architecture/CONTENT_PIPELINE.md`) unless a task
  explicitly says otherwise and has been approved.
- No MCP tool should delete assets or overwrite `.umap` files without an
  explicit, task-level approval (see `CLAUDE.md`).
- Prefer read/inspect tools before write tools when uncertain about current
  state.
- No MCP tool should write to backend tables representing real
  money/tenant relationships (`mall_leases`) — see
  `Docs/Architecture/BACKEND_INTEGRATION.md`.
