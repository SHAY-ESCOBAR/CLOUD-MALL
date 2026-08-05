# Roadmap

Status legend: `[ ]` not started · `[~]` in progress · `[x]` done

## Phase 1 — Repository Foundation
- [x] Repository branch (`feature/project-foundation`)
- [x] Documentation
- [x] Git LFS
- [x] Validation (GitHub Actions workflow)
- [x] Branch strategy

## Phase 2 — Unreal Project Creation
- [ ] Create `.uproject` (Unreal Engine 5)
- [ ] Configure required plugins
- [ ] Create a basic map
- [ ] Confirm `Content/` folder layout matches this repo
- [ ] Verify Play In Editor works

## Phase 3 — Claude Code Integration
- [ ] Install Claude Code on the local Unreal machine
- [ ] Confirm `CLAUDE.md` rules are being followed
- [ ] Confirm working-directory permissions
- [ ] Confirm Setup/Validation scripts run cleanly
- [ ] Run first end-to-end test task

## Phase 4 — Unreal MCP
- [ ] Install Unreal MCP server/plugin
- [ ] Establish local connection from Claude Code
- [ ] Enumerate available MCP tools
- [ ] Test: spawn/inspect an Actor
- [ ] Test: open/inspect a Map
- [ ] Test: create/inspect a Blueprint

## Phase 5 — Mall Reference-to-Blockout
- [ ] Reference material for mall layout (images/sketches/dimensions)
- [ ] Estimated dimension extraction (corridors, store units, atrium)
- [ ] Cross-reference layout with existing `mall_units` data (floor/zone/
      unit_code) from the Supabase project, so the 3D layout and real
      leasing data agree — see `Docs/Architecture/BACKEND_INTEGRATION.md`
- [ ] Blockout generation
- [ ] Camera framing / navigation pass
- [ ] Screenshot capture for review
- [ ] Human review checkpoint

## Phase 6 — Production Scene
- [ ] Meshes (storefronts, signage, fixtures)
- [ ] Materials
- [ ] Lighting
- [ ] Navigation/interaction Blueprints
- [ ] Store browsing interactions
- [ ] Optimization

## Phase 7 — Backend Integration (separate approval required for writes)
- [x] Backend chosen: reuse existing Supabase project from
      `cyber-solar-nexus` (project ref `qubbzwbtvuvpbcaasjmz`) — see
      `Docs/Architecture/BACKEND_INTEGRATION.md`
- [ ] Read-only integration: Unreal fetches `products` / `store_scenes` /
      `mall_units` via Supabase REST (anon key + RLS)
- [ ] Auth: Unreal client authenticates against the same Supabase Auth
      used by the web app (shared `user_roles`)
- [ ] Cart/checkout UI in Unreal (mock first, no write access)
- [ ] Sandboxed write-path testing (leases, purchases) in a non-production
      Supabase branch/project if available
- [ ] Explicit go-live approval before any real transaction or lease
      write path is enabled from Unreal

## Phase 8 — Automated Validation
- [ ] Self-hosted GitHub Actions runner (Windows + Unreal Engine 5)
- [ ] Unreal command-line validation
- [ ] Blueprint compile checks
- [ ] Map integrity checks
- [ ] Packaging smoke test
