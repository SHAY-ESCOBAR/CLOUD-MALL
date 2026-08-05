# Reference-to-Scene Workflow (Planned) — CLOUD MALL

This describes the future end-to-end flow once Phases 2-7 of `ROADMAP.md`
are complete. Nothing here is implemented yet.

1. **Upload reference** — mall layout image/video/sketch, store list,
   dimensions, and/or functional requirements (e.g. "two-level atrium,
   12 store units, food court").
2. **Store the reference** — saved under
   `Content/CORE_AI/References/<area-name>/` (e.g. `Atrium`,
   `StoreUnit_A`, `FoodCourt`).
3. **Create an Issue** — using the `Scene Build` template, linking to the
   stored reference.
4. **Analyze the reference** — Claude Code reviews the material and extracts
   purpose, approximate dimensions, required interactions (browsing,
   entering stores, checkout triggers), lighting, materials, performance
   targets.
5. **Document assumptions** — anything that cannot be determined from the
   reference is written down explicitly (per `CLAUDE.md` rule 6).
6. **Create a branch** — `scene/<area-name>` off `cloud-mall` (or `develop`
   once that branch exists).
7. **Blockout** — rough geometry at real-world scale (1 cm = 1 Unreal Unit).
8. **Review screenshots** — captured from the Editor, attached to the
   Issue/PR.
9. **Approval** — human sign-off before proceeding past blockout.
10. **Production build** — meshes, materials, lighting, Blueprints,
    navigation/store interactions, optimization.
11. **Purchase flow (separate track)** — only after Phase 7's approval gate;
    never bundled into a routine scene-build PR.
12. **Tests** — `Scripts/Validation/validate-repository.ps1` and, later,
    self-hosted Unreal CLI validation.
13. **Pull Request** — using `.github/pull_request_template.md`.
14. **Merge** — into the integration branch, then eventually `main`.
15. **Release** — tagged release once stable.
