# Roadmap

Status legend: `[ ]` not started · `[~]` in progress · `[x]` done

## Phase 1 — Repository Foundation
- [x] Repository branch (`cloud-mall`)
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

## Phase 7 — Real Purchase Integration (separate approval required)
- [ ] Choose e-commerce/payment backend
- [ ] Product catalog data source
- [ ] Cart/checkout UI (mock first)
- [ ] Sandboxed payment testing
- [ ] Explicit go-live approval before any real transaction path

## Phase 8 — Automated Validation
- [ ] Self-hosted GitHub Actions runner (Windows + Unreal Engine 5)
- [ ] Unreal command-line validation
- [ ] Blueprint compile checks
- [ ] Map integrity checks
- [ ] Packaging smoke test
