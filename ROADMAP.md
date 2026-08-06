# Roadmap

Status legend: `[ ]` not started · `[~]` in progress · `[x]` done

This roadmap follows the phased plan from `Docs/PROJECT_VISION.md`
(the "Shay Virtual Mall" specification), adopted into this repository
per `Docs/Decisions/ADR-002-SHAY-VIRTUAL-MALL-SCOPE.md`.

## Phase 0 — Environment Check
- [x] Repository branch (`feature/project-foundation`) + GitHub foundation
- [x] Git / Git LFS confirmed working locally
- [x] Unreal Engine confirmed installed locally (5.8)
- [ ] Visual Studio / Rider / build tools — not yet verified
- [ ] Unreal Automation Tool, Python Editor Script Plugin, Editor Utility
      Widgets — not yet verified as enabled
- [ ] Claude Code installed on the local Unreal machine (this session
      runs remotely — a local bridge is required, see
      `Docs/Architecture/MCP_ARCHITECTURE.md`)

## Phase 1 — Architecture Documents
- [x] `Docs/PROJECT_VISION.md`
- [x] `Docs/Architecture/UNREAL_GAME_ARCHITECTURE.md`
- [x] `Docs/Architecture/DATA_MODEL.md`
- [x] `Docs/Architecture/CONTENT_PIPELINE.md`
- [x] `Docs/Architecture/MCP_ARCHITECTURE.md` (Unreal Automation Plan)
- [x] `Docs/TASKS.md`
- [x] This roadmap

## Phase 2 — Unreal Project Creation
- [x] Create `.uproject` (Unreal Engine 5.8) — `CLOUDMALL.uproject`,
      verified present at the repo root on `feature/project-foundation`
      (2026-08-06). Internal project name is `CLOUDMALL`, not
      `ShayVirtualMall` — Unreal doesn't allow hyphens in project names,
      and the folder had to match the existing repo folder name
      (`CLOUD-MALL`) exactly for the project to land at the repo root
      instead of a nested subfolder. Renaming the display name is
      possible later via Project Settings if desired; not done yet.
- [ ] Configure required plugins
- [ ] Confirm `Content/` folder layout matches
      `Docs/Architecture/UNREAL_GAME_ARCHITECTURE.md` (skeleton exists;
      not yet verified inside the Unreal Editor itself)
- [ ] Verify Play In Editor works on an empty map

## Phase 3 — Greybox MVP
No investment in final art yet — validate scale, flow, and interactions:
- [ ] Exterior mall entrance structure
- [x] Central lobby (Atrium greybox, 24m x 24m)
- [x] Main corridor (extended to X=6000 to reach the Flagship Anchor bay)
- [x] Three storefronts: technology / fashion / café (plus a 4th,
      Flagship Anchor, added past MVP scope per Docs/Architecture/
      TENANT_MIX_PLAN.md)
- [ ] At least one store fully active/enterable
- [ ] First-person keyboard+mouse movement (real walking — flying
      spectator confirmed working today, see Docs/TASKS.md)
- [ ] Automatic doors
- [ ] Basic information point + signage
- [ ] Basic dynamic lighting

## Phase 4 — Interaction System
- [ ] `BPI_Interactable` interface
- [ ] `BP_InteractionComponent`
- [ ] `BP_ProductActor`
- [ ] `WBP_InteractionPrompt`
- [ ] `WBP_ProductDetails`
- [ ] `BP_StoreTrigger`
- [ ] `BP_AutomaticDoor`

## Phase 5 — Data-Driven Stores
- [ ] Data Assets/Tables for products, stores, promotions, shelf
      positions, signage positions (see `Docs/Architecture/DATA_MODEL.md`)
- [ ] Load products without opening a Blueprint or changing code

## Phase 6 — UI
- [ ] Minimal crosshair/reticle
- [ ] Interaction prompt
- [ ] Product card
- [ ] Shopping cart (local/mock)
- [ ] Mall map
- [ ] Main menu, settings, loading screen
- [ ] Save player position/settings

## Phase 7 — Visual Quality
Only after the systems above work:
- [ ] Replace greybox with real assets (see
      `Docs/Architecture/CONTENT_PIPELINE.md`)
- [ ] Nanite where appropriate
- [ ] Lumen per hardware targets
- [ ] Glass / metal / concrete / wood / fabric / floor materials
- [ ] Reflections, store lighting, lit signage, greenery
- [ ] Performance budget per zone, checked before adding more assets

## Phase 8 — Editor Automation
- [ ] Store-from-template creation tool
- [ ] Store category selection
- [ ] Auto storefront generation
- [ ] Shelf/product-point placement
- [ ] Store Configuration loading
- [ ] Logo/brand color swap
- [ ] Signage generation
- [ ] Error checking
- [ ] Test build generation
- [ ] The MCP/Unreal Control Layer itself (`Docs/Architecture/MCP_ARCHITECTURE.md`):
      spawn/inspect Actor, open/inspect Map, create/inspect Blueprint,
      read logs, screenshots, run build, report errors back

## Phase 9 — External System Integration (separate approval required for writes)
- [x] Backend chosen: reuse existing Supabase project from
      `cyber-solar-nexus` (project ref `qubbzwbtvuvpbcaasjmz`) — see
      `Docs/Architecture/BACKEND_INTEGRATION.md`
- [x] First 10 stores seeded into `mall_units` (catalog only, no leases)
- [ ] Read-only integration: Unreal fetches `products` / `store_scenes` /
      `mall_units` via Supabase REST (anon key + RLS)
- [ ] Auth: Unreal client authenticates against the same Supabase Auth
      used by the web app (shared `user_roles`)
- [ ] Cart/checkout UI in Unreal — **mock data and mock checkout only**
      at this stage, no real payment integration
- [ ] Analytics event system (foot traffic / views / interactions)
- [ ] Business-owner dashboard hook (product upload, store management)
- [ ] Explicit go-live approval before any real transaction, lease write,
      or payment path is enabled from Unreal

## Phase 10 — Automated Validation
- [ ] Self-hosted GitHub Actions runner (Windows + Unreal Engine 5)
- [ ] Unreal command-line validation
- [ ] Blueprint compile checks
- [ ] Map integrity checks
- [ ] Packaging smoke test
