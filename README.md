# CLOUD MALL — Shay Virtual Mall

## Vision

A virtual, walkable shopping mall built in **Unreal Engine 5** (internal
project name `ShayVirtualMall`), driven by natural-language instructions,
visual references, Claude Code, and MCP — where visitors can browse
stores and **actually complete real online purchases** inside the 3D
environment.

The long-term product isn't "one mall" — it's a system that generates and
operates 3D malls and stores for businesses, each with its own space, AI
agent, products, promotions, and analytics. See `Docs/PROJECT_VISION.md`
for the full vision and `Docs/Decisions/ADR-002-SHAY-VIRTUAL-MALL-SCOPE.md`
for why this expanded spec lives here rather than in a new repository.

This project follows the same GitHub-first approach established in
`CORE-Unreal-AI`: infrastructure, documentation, and version control come
first, 3D content comes after.

**Backend decision (2026-08-05):** rather than build a new purchase
backend, this project connects to the existing Supabase project already
built for `cyber-solar-nexus` — a sibling repo with a working
browser-based 3D mall (real product catalog, cart, wallet, and a
120-unit mall leasing system with real ILS rent data). See
`Docs/Architecture/BACKEND_INTEGRATION.md`.

## Documentation map

| Doc | Covers |
|---|---|
| `Docs/PROJECT_VISION.md` | Product/business vision |
| `Docs/Architecture/SYSTEM_ARCHITECTURE.md` | GitHub-first pipeline architecture |
| `Docs/Architecture/UNREAL_GAME_ARCHITECTURE.md` | Mall Kit, core game systems, folder layout |
| `Docs/Architecture/DATA_MODEL.md` | Product / Store / Mall data structures |
| `Docs/Architecture/CONTENT_PIPELINE.md` | Reference → greybox → production asset flow |
| `Docs/Architecture/MCP_ARCHITECTURE.md` | The Unreal Control Layer / automation plan |
| `Docs/Architecture/BACKEND_INTEGRATION.md` | The shared Supabase backend |
| `ROADMAP.md` | Phase 0–10 plan |
| `Docs/TASKS.md` | Current concrete checklist |

## Current Status

**Foundation and documentation in place; no `.uproject` or 3D content
yet.** See `Docs/TASKS.md` for what's next (Unreal project creation is
the current blocking step, owned by the local machine).

## Safety Principles

- Never overwrite existing maps.
- Never delete assets without explicit approval.
- All new AI-generated work stays inside `Content/CORE_AI/`.
- Commit before any significant change.
- Never commit credentials, tokens, API keys, or payment/checkout secrets.
- Blockout first, production detail only after review/approval.
- No real payment integration goes live without explicit, separate approval.
- No write access to the Supabase `mall_units`/`mall_leases` tables (real
  tenant/rent data) from AI-driven automation without the same approval
  gate as payments — see `Docs/Architecture/BACKEND_INTEGRATION.md`.
- Never claim an Unreal Editor action was performed if it actually wasn't
  — see `Docs/Architecture/MCP_ARCHITECTURE.md`.

## Repository Structure

```
CLOUD-MALL/
├── .github/                 GitHub Actions, issue templates, PR template
├── Config/                  Unreal engine/project config (.ini)
├── Content/
│   ├── CORE_AI/              AI-generated / AI-managed content (see CLAUDE.md)
│   ├── Mall/                 Architecture, Materials, Props, Lighting, Stores,
│   │                         Products, Navigation, Advertising
│   └── Core/                 Blueprints, Components, Interfaces, Data, UI, Save, Audio
├── Plugins/                 Unreal plugins (MCP bridge, editor utilities, etc.)
├── Scripts/                 Setup, validation, Unreal editor, and MCP scripts
├── Source/ShayVirtualMall/  C++ source: Core, Interaction, Commerce, Navigation, AI, Data
├── Tests/                   Automated tests
├── Tools/                   Standalone tooling
└── Docs/                    Architecture, setup, workflow, and decision records
```

See `Docs/Architecture/UNREAL_GAME_ARCHITECTURE.md` for the full folder
layout including `Characters/` and `Maps/`.

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
folder structure, targeting **Unreal Engine 5.8**, internal project name
`ShayVirtualMall`.

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
