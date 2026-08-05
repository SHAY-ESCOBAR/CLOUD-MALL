# CLAUDE.md — Working Rules for This Repository

These rules are permanent for any Claude Code session working in
`CLOUD-MALL`. They apply regardless of which specific task is requested.

## Before doing anything

1. Read `README.md` and the relevant files under `Docs/` first.
2. Do not modify files unrelated to the current task.

## Assets and content

3. Never delete assets without explicit user approval.
4. All new AI-generated content goes inside `Content/CORE_AI/` — never
   scattered elsewhere in `Content/`.
5. Never use placeholder names like `NewBlueprint`, `Cube1`, or `Material2`.
   Use descriptive names that say what the thing is (e.g.
   `BP_StoreEntrance_AnchorNorth`, not `BP_Door2`).
6. Document any assumption you made that could not be proven from the
   supplied reference material.
7. Never overwrite `.umap` files.
8. Do blockout before detailed/production building.
9. Keep real-world scale: 1 cm = 1 Unreal Unit.
10. Keep Logic, Visuals, UI, and Generated Content separated (see
    `Content/CORE_AI/` subfolder structure).
11. Create documentation for every asset generated automatically.

## Money and real purchases (specific to this project)

12. Never wire up a real payment/checkout flow to move real money without
    explicit, separate, written approval for that specific step. Blockout
    and UI mockups for checkout are fine; live payment processing is not,
    by default.
13. Never commit payment provider secrets, API keys, or test/live tokens.
14. Treat any product/pricing data as needing a documented source — no
    invented prices presented as real.

## Git and branches

15. Never modify `main` directly. Always work in a feature branch.
16. Create small, clear commits — one logical step per commit.
17. Never force-push.
18. Never run `git reset --hard` without explicit approval.
19. Never run `git clean -fd` without explicit approval.
20. Run available tests/validation before committing.
21. Show a diff summary before pushing.

## Secrets

22. Never commit secrets, tokens, API keys, or credentials of any kind.

## When in doubt

If a request conflicts with any rule above, stop and ask rather than
guessing or working around the rule.
