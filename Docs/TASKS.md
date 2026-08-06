# Tasks — Near-Term

Live task list. Check items off as they're actually done — not planned,
done. Cross-reference `ROADMAP.md` for the full phased plan.

## Phase 0 — Environment (owner action required, local machine)
- [ ] Run `Scripts/Setup/setup-project.ps1` and paste the output back
- [ ] Confirm Visual Studio or Rider is installed (needed for C++ builds
      if/when Source/ code is added)
- [ ] Confirm Editor Scripting Utilities plugin can be enabled in a test
      project

## Phase 2 — Unreal Project Creation — DONE (2026-08-06)
- [x] `git clone -b feature/project-foundation` this repo locally
- [x] Unreal → New Project → Blank template → `CLOUDMALL.uproject`
      created at the repo root
- [x] Confirmed `Content/`, `Config/` sit next to the `.uproject`
- [x] Committed the `.uproject` + `Config/` on this branch (not `main`)
- [x] `Docs/Setup/UNREAL_SETUP.md` updated with final confirmed details

## Phase 3 — Greybox (current focus)
- [x] Opened `CLOUDMALL.uproject`, Editor loads without errors
- [x] Created `Content/Maps/Development/DEV_EmptyLevel.umap` — a genuinely
      empty level (0 actors), replacing the default demo/landscape map
      Unreal ships with new projects
- [x] Set as both Editor Startup Map and Game Default Map
      (Project Settings → Maps & Modes)
- [x] Committed and pushed — verified on GitHub as a 129-byte LFS pointer
      (confirms `.umap` is correctly routed through Git LFS, not stored
      as a raw blob)
- [x] Verify Play In Editor works on `DEV_EmptyLevel` — confirmed via
      Editor log, 2 successful PIE sessions ("PIE: Play in editor total
      start time..."), no errors/crashes — 2026-08-06
- [x] Block out entrance + lobby + main corridor (Atrium + corridor floors
      and walls placed via `Scripts/Unreal/phase3_greybox_floors.py` +
      `phase3_greybox_walls.py`, confirmed via Editor log — 2026-08-06)
- [x] Block out 3 storefronts (technology / fashion / café) — placed via
      `Scripts/Unreal/phase3_greybox_bays.py`, confirmed via screenshot
      (divider actor `SM_BayDivider_TechnologyFashion_Greybox` with the
      exact expected transform) — 2026-08-06
- [x] Cleaned up duplicate greybox actors (floors placed multiple times
      by re-running `phase3_greybox_floors.py`) via
      `Scripts/Unreal/cleanup_duplicate_greybox_actors.py` — confirmed
      via Editor log, 4 duplicates removed — 2026-08-06
- [x] Ground floor expansion: 1 Flagship Anchor bay (24m) placed east of
      Cafe via `Scripts/Unreal/groundfloor_flagship_anchor.py`, corridor
      extended to X=6000 — confirmed via Editor log — 2026-08-06
- [x] PlayerStart placed at the mall entrance via
      `Scripts/Unreal/phase3_playerstart.py` — confirmed via Editor log
      — 2026-08-06
- [ ] Follow-up: storefront-facing wall/glass/door per bay (currently
      fully open on all 4 bays including the new anchor), a ceiling, and
      picking which `mall_units` rows these bays represent (not decided)
- [ ] Pick which one store becomes the first fully-active one
- [ ] Real walking first-person movement — path chosen: Epic's built-in
      "First Person" content pack (not a hand-built Blueprint) + setting
      it as Default Pawn Class. Manual step, not yet done — see
      `phase3_playerstart.py`'s docstring for exact steps.
      Confirmed already: the default flying spectator pawn (Blank
      template ships with one) works for Play-In-Editor today — press
      Play, click into the viewport, WASD + mouse, E/Q for up/down.
- [ ] Screenshot the result (Top view) for review before moving to Phase 4

## Not started, tracked for later
- Interaction system (Phase 4)
- Data-driven store loading (Phase 5)
- UI (Phase 6)
- Visual quality pass (Phase 7)
- Editor automation tool + MCP bridge (Phase 8)
- Supabase read integration (Phase 9)
