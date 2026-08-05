# Tasks — Near-Term

Live task list. Check items off as they're actually done — not planned,
done. Cross-reference `ROADMAP.md` for the full phased plan.

## Phase 0 — Environment (owner action required, local machine)
- [ ] Run `Scripts/Setup/setup-project.ps1` and paste the output back
- [ ] Confirm Visual Studio or Rider is installed (needed for C++ builds
      if/when Source/ code is added)
- [ ] Confirm Editor Scripting Utilities plugin can be enabled in a test
      project

## Phase 2 — Unreal Project Creation
- [ ] `git clone -b feature/project-foundation` this repo locally (if not
      already done)
- [ ] Unreal → New Project → **Blank** template → Location = the repo
      clone → Name = `ShayVirtualMall`
- [ ] Confirm `Content/`, `Config/` sit next to the new `.uproject`
- [ ] Commit the `.uproject` + `Config/` on this branch (not `main`)
- [ ] Report back so `Docs/Setup/UNREAL_SETUP.md` can be updated with the
      final confirmed details

## Phase 3 — Greybox (blocked on Phase 2)
- [ ] Block out entrance + lobby + main corridor
- [ ] Block out 3 storefronts (technology / fashion / café)
- [ ] Pick which one store becomes the first fully-active one
- [ ] Basic first-person movement working
- [ ] Screenshot the result for review before moving to Phase 4

## Not started, tracked for later
- Interaction system (Phase 4)
- Data-driven store loading (Phase 5)
- UI (Phase 6)
- Visual quality pass (Phase 7)
- Editor automation tool + MCP bridge (Phase 8)
- Supabase read integration (Phase 9)
