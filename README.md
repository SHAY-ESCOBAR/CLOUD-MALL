# CLOUD MALL

## Vision

A virtual, walkable shopping mall built in **Unreal Engine 5**, driven by
natural-language instructions, visual references, Claude Code, and MCP —
where visitors can browse stores and **actually complete real online
purchases** inside the 3D environment (not a cosmetic showcase — a working
storefront layer on top of real e-commerce).

This project follows the same GitHub-first approach established in
`CORE-Unreal-AI`: infrastructure, documentation, and version control come
first, 3D content comes after.

**Backend decision (2026-08-05):** rather than build a new purchase
backend, CLOUD MALL connects to the existing Supabase project already
built for `cyber-solar-nexus` — a Lovable-originated web app that already
implements a browser-based 3D mall with a real product catalog, cart,
wallet, and a 120-unit mall leasing system (real ILS rent data). See
`Docs/Architecture/BACKEND_INTEGRATION.md`.

## Main Capabilities (target state)

- Reference analysis (mall layout references, store photos, sketches,
  dimensions, functional requirements)
- Unreal blockout generation (corridors, store units, atrium, anchor stores)
- Procedural scene building
- Blueprint generation (navigation, store interaction, checkout triggers)
- Material and lighting creation
- Real purchase flow integration, backed by the existing `cyber-solar-nexus`
  Supabase project (see `Docs/Architecture/BACKEND_INTEGRATION.md`)
- AI-assisted environment production
- GitHub version control for every generated change
- Validation and rollback at every stage
- Documentation of generated assets

## Current Status

**Foundation and repository setup.** No 3D content, Unreal project, mall
layout, or store data exists yet. This repository currently establishes
structure, documentation, version control, and the connection plan to
Unreal Engine 5, MCP, and the existing Supabase backend.

## Planned Architecture

- GitHub repository (this branch) — source of truth, history, review, rollback
- Local Unreal Engine 5 installation — the engine runs on your machine, never in CI
- Claude Code — orchestrates analysis, planning, and file/asset generation
- Unreal MCP server or plugin — the bridge Claude Code uses to control the Editor
- Python Editor Scripting / Editor Scripting Utilities — in-Editor automation
- Blueprint automation
- Existing Supabase project (from `cyber-solar-nexus`) as the purchase/mall
  backend that the in-world storefronts call into — see
  `Docs/Architecture/BACKEND_INTEGRATION.md`
- GitHub Actions — repository-level validation (see `.github/workflows`)

See `Docs/Architecture/SYSTEM_ARCHITECTURE.md` for details.

## Safety Principles

- Never overwrite existing maps.
- Never delete assets without explicit approval.
- All new AI-generated work stays inside `Content/CORE_AI/`.
- Commit before any significant change.
- Never commit credentials, tokens, API keys, or payment/checkout secrets.
- Blockout first, production detail only after review/approval.
- No real payment integration goes live without explicit, separate approval
  — this is a hard line given real money will be involved eventually.
- No write access to the Supabase `mall_units`/`mall_leases` tables (real
  tenant/rent data) from AI-driven automation without the same approval
  gate as payments — see `Docs/Architecture/BACKEND_INTEGRATION.md`.

## Repository Structure

```
CLOUD-MALL/
├── .github/                 GitHub Actions, issue templates, PR template
├── Config/                  Unreal engine/project config (.ini)
├── Content/CORE_AI/         All AI-generated / AI-managed content lives here
├── Plugins/                 Unreal plugins (MCP bridge, editor utilities, etc.)
├── Scripts/                 Setup, validation, Unreal editor, and MCP scripts
├── Source/                  C++ source (if/when the project needs it)
├── Tests/                   Automated tests
├── Tools/                   Standalone tooling
└── Docs/                    Architecture, setup, workflow, and decision records
```

## Setup

### 1. Clone the repository
```bash
git clone -b feature/project-foundation https://github.com/SHAY-ESCOBAR/CLOUD-MALL.git
cd CLOUD-MALL
```

### 2. Install Git LFS
```bash
git lfs install
git lfs pull
```

### 3. Open the project in Unreal
No `.uproject` file exists yet — this is intentional. See
`Docs/Setup/UNREAL_SETUP.md` for how to create one against this repo's
folder structure, targeting **Unreal Engine 5**.

### 4. Install required plugins
See `Docs/Setup/UNREAL_SETUP.md` for the plugin list once defined. Do not
install unfamiliar/unverified plugins.

### 5. Install Claude Code
Run it from the root of this repository so it picks up `CLAUDE.md`.

### 6. Connect MCP
See `Docs/Architecture/MCP_ARCHITECTURE.md` and
`Scripts/MCP/test-mcp-connection.ps1` (currently a skeleton).

### 7. Verify the connection
Run `Scripts/Validation/validate-repository.ps1` before starting work.

### 8. Create a development branch
```bash
git checkout -b feature/<your-feature-name>
```
Never commit directly to `main`. See `Docs/Workflows/BRANCHING_WORKFLOW.md`.

## License

See `LICENSE`.
