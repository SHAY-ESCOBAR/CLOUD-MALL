# Contributing

## Branch strategy

- `main` — stable releases only. Never commit directly.
- `develop` — integration branch.
- `feature/*` — new capabilities.
- `scene/*` — environment/scene building.
- `fix/*` — bug fixes.
- `docs/*` — documentation-only changes.
- `experiment/*` — throwaway experiments; may be deleted without notice.

See `Docs/Workflows/BRANCHING_WORKFLOW.md` for the full workflow.

## Commits

- Small, focused, descriptive commits.
- Conventional prefixes are encouraged: `feat:`, `fix:`, `docs:`, `chore:`,
  `refactor:`, `test:`.

## Before opening a Pull Request

- Run `Scripts/Validation/validate-repository.ps1`.
- Fill out the PR template completely, including the checklist.
- No secrets, no temp files, no unmanaged large binaries.
- Confirm the map opens and there are no Blueprint compile errors, if
  applicable to your change.

## Asset naming

- Descriptive names only. No `NewBlueprint`, `Cube1`, `Material2`, etc.
- All AI-generated content belongs under `Content/CORE_AI/`.

## Code of conduct

Be respectful and constructive in issues, PRs, and reviews.
