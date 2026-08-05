# Content Pipeline

Status: **planned**. Describes how content moves from reference material
to a finished in-Unreal asset, and where AI-assisted generation fits.

## Stages

1. **Reference intake** — image, video, sketch, dimensions, or text
   description, saved under `Content/CORE_AI/References/<item-name>/`.
2. **Greybox first** — see Phase 3 in `ROADMAP.md`. Rough geometry at
   real-world scale (1 cm = 1 Unreal Unit), no final materials/lighting.
   Purpose: validate scale, layout, flow, and interactions before
   investing in final art.
3. **AI-assisted asset generation (optional, evaluated per-asset)** —
   for props/meshes/materials where an AI generation tool is used (e.g. a
   text-to-3D or image-to-3D tool), output lands in
   `Content/CORE_AI/Generated/` first for review, **not** directly into
   `Content/Mall/` — see `Docs/Architecture/UNREAL_STRUCTURE.md`. No
   specific AI generation tool is chosen yet; document whichever is
   adopted here once decided, including license terms (per `CLAUDE.md`
   rule against commercial assets without a verified license).
4. **Review checkpoint** — screenshots captured, human review, per
   `Docs/Workflows/REFERENCE_TO_SCENE.md`.
5. **Promotion to production folders** — approved assets move from
   `Content/CORE_AI/Generated/` into the appropriate `Content/Mall/*`
   subfolder (Architecture / Materials / Props / Lighting / Stores /
   Products / Navigation / Advertising), with descriptive names (never
   `NewBlueprint`/`Cube1`/`Material2` — `CLAUDE.md` rule 5).
6. **Optimization pass** — Nanite/Lumen where appropriate, LOD, texture
   budgets — only after the system/gameplay behavior is validated, per
   Phase 7 in `ROADMAP.md`.

## Assumptions to revisit

- No AI 3D-asset generation tool is selected yet. Do not assume a
  specific one (Meshy/Luma/Rodin/etc.) is in use until it's actually
  chosen and documented here.
- No real product photography/3D scans exist yet for the MVP's three
  stores (tech / fashion / café). Placeholder or licensed stock assets
  should be clearly marked as temporary in their own naming/folder
  (`Content/CORE_AI/References/` or a `_Placeholder` suffix), not mixed
  silently with final assets.
