# ADR-002: Adopt the "Shay Virtual Mall" Specification Into `CLOUD-MALL`

## Status

Accepted — 2026-08-05

## Context

A much more detailed specification ("SHAY VIRTUAL MALL") was produced
(via a video walkthrough summarized by another AI tool) describing a
modular, data-driven Unreal Engine mall system — first-person navigation,
Data Asset–driven stores/products, an Editor automation layer, and a
longer-term "mall-generation-as-a-service" business model.

This overlaps heavily with the `CLOUD-MALL` foundation already
established: same GitHub-first approach, same Unreal Engine 5 target,
same blockout-before-production principle, same eventual MCP/automation
bridge. The project had already fragmented once before (`CORE-Unreal-AI`
→ `CLOUD-MALL` → `cyber-solar-nexus`, plus an accidental throwaway repo),
causing real confusion (wrong local folders, redundant branches).

## Decision

Adopt the Shay Virtual Mall specification **as an upgrade to
`CLOUD-MALL`'s own documentation and roadmap**, not as a new repository.
The Unreal project itself (the `.uproject`, once created) may be named
`ShayVirtualMall` internally — that is cosmetic and does not require a
separate GitHub repository.

## Consequences

- `Docs/PROJECT_VISION.md`, `Docs/Architecture/UNREAL_GAME_ARCHITECTURE.md`,
  `Docs/Architecture/DATA_MODEL.md`, `Docs/Architecture/CONTENT_PIPELINE.md`,
  and `Docs/Architecture/MCP_ARCHITECTURE.md` (expanded into the
  automation plan) are added/rewritten in this repo.
- `ROADMAP.md` is restructured around the Phase 0–9 plan from the
  specification (environment check → architecture docs → project creation
  → greybox → interaction system → data-driven stores → UI → visual
  quality → automation → external system integration).
- `cyber-solar-nexus` remains the separate, already-live browser version
  and shares the same Supabase backend (`Docs/Architecture/BACKEND_INTEGRATION.md`)
  — it is not merged into this repo; the two stay complementary (web vs.
  native Unreal).
- No further new mall-related repositories should be created without an
  explicit ADR justifying why consolidation isn't possible.
