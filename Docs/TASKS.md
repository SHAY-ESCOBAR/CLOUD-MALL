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
- [ ] Open `CLOUDMALL.uproject`, confirm the Editor loads without errors
- [ ] Verify Play In Editor works on the default/empty map
- [ ] Block out entrance + lobby + main corridor
- [ ] Block out 3 storefronts (technology / fashion / café)
- [ ] Pick which one store becomes the first fully-active one
- [ ] Basic first-person keyboard+mouse movement
- [ ] Screenshot the result for review before moving to Phase 4

## Not started, tracked for later
- Interaction system (Phase 4)
- Data-driven store loading (Phase 5)
- UI (Phase 6)
- Visual quality pass (Phase 7)
- Editor automation tool + MCP bridge (Phase 8)
- Supabase read integration (Phase 9)
