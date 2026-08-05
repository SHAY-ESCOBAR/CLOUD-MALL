# MCP Architecture

## Status

Not yet installed. This document is the plan to be filled in once an Unreal
MCP server/plugin is chosen and installed locally (Phase 4 of `ROADMAP.md`).

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

## Safety constraints for any MCP tool call

- Every MCP-driven change must be inside `Content/CORE_AI/` unless a task
  explicitly says otherwise and has been approved.
- No MCP tool should delete assets or overwrite `.umap` files without an
  explicit, task-level approval (see `CLAUDE.md`).
- Prefer read/inspect tools before write tools when uncertain about current
  state.
