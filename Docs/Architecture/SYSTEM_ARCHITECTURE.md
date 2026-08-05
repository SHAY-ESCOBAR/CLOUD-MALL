# System Architecture — CLOUD MALL

## Overview

CLOUD MALL is a GitHub-first pipeline (same pattern as `CORE-Unreal-AI`)
for building a virtual, walkable shopping mall in Unreal Engine 5 where
visitors can browse and complete real purchases.

```
Reference material (mall layout, store list, product data)
      |
      v
GitHub Issue (Scene Build / AI Generation Task)
      |
      v
Claude Code (analysis, planning, assumption documentation)
      |
      v
Unreal MCP bridge  <-- runs locally, talks to the local Unreal Editor
      |
      v
Local Unreal Engine 5 Editor (Blockout -> Production)
      |
      v
Commit to feature/scene branch, screenshots, docs
      |
      v
Pull Request -> review -> merge -> release
```

## Components

| Component | Where it runs | Responsibility |
|---|---|---|
| GitHub repository/branch | GitHub | Source of truth, history, issues, PRs, CI validation |
| Claude Code | Local machine (or this session) | Reads references/issues, plans, edits repo files, drives MCP calls |
| Unreal MCP server/plugin | Local machine, alongside Unreal Editor | Exposes Editor operations as MCP tools |
| Unreal Engine 5 Editor | Local machine only | Renders/builds the mall. Never runs in GitHub Actions. |
| GitHub Actions (`repository-validation.yml`) | GitHub-hosted runner | Structure/docs/secrets/LFS/JSON/YAML/Markdown checks |
| Self-hosted runner (future) | Local Windows machine with Unreal installed | Blueprint compile checks, map load checks, packaging smoke tests |
| Purchase/mall backend | Existing Supabase project (from `cyber-solar-nexus`) | Product catalog, cart/wallet, mall unit/lease data, auth — called from in-world storefronts. See `Docs/Architecture/BACKEND_INTEGRATION.md` |

## Reused backend (decision, 2026-08-05)

Rather than choosing a new e-commerce/payment backend, CLOUD MALL reuses
the Supabase project already built for `cyber-solar-nexus` (a Lovable-
originated web app that is itself a browser-based 3D mall with real
cart/wallet/store/lease data). Full details, table schema, and the safety
rules around it: `Docs/Architecture/BACKEND_INTEGRATION.md`.

## Non-goals (for now)

- Running Unreal Engine inside GitHub Actions / any public cloud runner.
- Fully automated merges to `main` without human review.
- Any live payment processing or mall-lease write operation without an
  explicit, separate approval step (see `CLAUDE.md` and
  `Docs/Architecture/BACKEND_INTEGRATION.md`).
