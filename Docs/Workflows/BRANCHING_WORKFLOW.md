# Branching Workflow

## Branches

| Branch | Purpose |
|---|---|
| `main` | Stable releases only. Protected. No direct commits. |
| `develop` | Integration branch for merged, working features. |
| `feature/*` | New capabilities (tooling, pipeline, non-scene features). |
| `scene/*` | Building a specific environment/scene. |
| `fix/*` | Bug fixes. |
| `docs/*` | Documentation-only changes. |
| `experiment/*` | Throwaway experiments. May be deleted without notice; never merged directly to `develop`/`main`. |

## Flow

1. Branch off `develop` (or `main` for the very first foundation work).
2. Small, descriptive commits.
3. Push the branch, open a PR using the repository's PR template.
4. `Repository Validation` GitHub Action must pass.
5. Human review and approval.
6. Merge into `develop`. Periodically, `develop` is merged into `main` as a
   release.

## Rules

- Never force-push a shared branch.
- Never rewrite history without explicit approval.
- Never commit directly to `main`.
- Keep PRs scoped to one logical change where possible.
