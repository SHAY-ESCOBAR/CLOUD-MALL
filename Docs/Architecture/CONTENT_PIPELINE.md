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

## Why "dressing" any future version stays easy

The layout (`Docs/Architecture/MALL_LAYOUT.md`) and the data model
(`Docs/Architecture/DATA_MODEL.md`) are **decoupled from visuals on
purpose**: a bay is a grid slot with a `unit_code`, not a specific mesh.
That means:

- Swapping which asset pack/material set dresses a bay never touches the
  grid, the Blueprints, or the data — only what's placed inside a slot
  that's already the right size (8×12 m per bay, per `MALL_LAYOUT.md`).
- Multiple visual "skins" can exist for the same layout (e.g. a cheap
  greybox-plus-basic-materials version now, a fully dressed version
  later) without redoing Phase 3–6 work.
- This is the same reason greybox comes before art (Phase 3 before
  Phase 7) — the grid gets validated once, dressing can change any number
  of times after.

## Phase 7 asset-pack candidates (not purchased, not decided — evaluate later)

Found via a marketplace search on 2026-08-06, kept here so they aren't
lost. **Not vetted for price, license terms, or actual 5.8 compatibility
— verify on the listing itself before any purchase.** Do not buy or
import any of these before Phase 3 (greybox) confirms the layout in
`MALL_LAYOUT.md` actually works — buying dressing for a layout that might
still change is wasted spend.

- [City Shopping Mall (MODULAR Environment) V1.5](https://unrealengine.com/marketplace/en-US/product/shopping-mall) —
  full modular mall (changeable length/width/floor count), includes
  elevator, escalator, doors/gates, fountain, barrier, roof AC. Closest
  match to this project's "always expandable" grid principle.
- [Shopping Mall Environment Kit](https://www.fab.com/listings/17ca68da-e6d1-4ad7-a455-33ddbaeeaa01) —
  mall structure + multiple store types, restrooms, cafés, described as
  AAA-quality modular meshes/props/decals.
- [Small Town Stores - Modular Pack](https://www.fab.com/listings/cfa3b6a2-427b-403a-9317-22450717cf53) —
  not an enclosed mall; an open modular storefront street (Lumen/Nanite).
  Worth revisiting if an open-air "street" variant is ever wanted instead
  of/alongside the enclosed mall.

## Assumptions to revisit

- No AI 3D-asset generation tool is selected yet. Do not assume a
  specific one (Meshy/Luma/Rodin/etc.) is in use until it's actually
  chosen and documented here.
- No real product photography/3D scans exist yet for the MVP's three
  stores (tech / fashion / café). Placeholder or licensed stock assets
  should be clearly marked as temporary in their own naming/folder
  (`Content/CORE_AI/References/` or a `_Placeholder` suffix), not mixed
  silently with final assets.
