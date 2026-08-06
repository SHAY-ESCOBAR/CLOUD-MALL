# Tenant Mix Plan — Full Mall Program (Future Scope)

Status: **planning document, not yet built**. This describes the
full-mall business/spatial model the owner wants to grow toward. It does
not change Phase 3's MVP scope (`Docs/TASKS.md`, `ROADMAP.md`: Atrium +
B1/B2/B3 + main corridor only) — it is the plan that MVP scope must stay
compatible with, same relationship `MALL_LAYOUT.md` already has to the
grid. Nothing here gets built without a separate, explicit go-ahead per
zone, same as every other phase in this repo.

## Why this exists

The owner's goal is not "a 3D mall demo" — it's an actual multi-category
retail business: global brand flagships, boutique fashion, and an
automotive anchor, growing into other retail verticals over time. This
document is the spatial + data-model translation of that goal, built on
top of the expandable grid already defined in `MALL_LAYOUT.md`.

## Floor program

### Ground floor (`G`, Z = 0cm) — Flagship anchors

`MALL_LAYOUT.md` already defines the unit for this: **Anchor store =
2–3 bay modules wide (16–24m)**. Ground floor is the natural home for
large-footprint global brand flagships — best foot traffic, most direct
atrium visibility, easiest loading/back-of-house access. No new grid unit
needed; this is already-specified, just not built.

### Level 2 (Z = 500cm) — Boutique

Reuses the atrium's vertical circulation core, which `MALL_LAYOUT.md`
already sized for future floors from day one specifically so this doesn't
require rebuilding the atrium. Standard single-bay modules (8m × 12m,
the existing "Base bay module" unit) — smaller, denser, boutique-format
units sit directly above the ground-floor corridor spine.

### Automotive anchor (car dealership) — documented exception, not standard grid

This does **not** fit the standard 5m floor-to-floor / 8×12m bay grid,
and forcing it to would be dishonest about what a car dealership actually
needs:

- Clear height: realistically 6–8m minimum for vehicle display + any
  lift equipment — roughly 1.5–2x the standard floor height.
- Much larger clear-span floor area than a 16–24m flagship bay, plus
  likely drive-in/service access separate from pedestrian corridor
  circulation.
- **Assumption, not confirmed**: best modeled as its own ground-floor
  wing branching off the atrium (the atrium is designed as a junction,
  not a dead end, precisely to support this kind of perpendicular
  extension per `MALL_LAYOUT.md`) rather than squeezed into the linear
  bay sequence. Exact placement/size needs a decision before any
  blockout starts.

## Data model / backend implication — needs separate approval

The existing shared Supabase `mall_zone` enum (from
`Docs/Architecture/BACKEND_INTEGRATION.md`: `market`, `fashion_anchor`,
`fashion_inline`, `tech_arena`, `social_zone`) has **no category yet**
for flagship-anchor, boutique-tier, or automotive. This schema is shared
with the live `cyber-solar-nexus` product — adding enum values is a
migration against a database another live product depends on, so per
`BACKEND_INTEGRATION.md`'s safety rules this is **not** something to do
as a side effect of this plan. It needs its own explicit approval step
before any migration is written, same as the existing `mall_units` seed
migration did.

## What this plan does NOT claim

- Does not claim any of this is built in Unreal — it isn't.
- Does not assume specific brands/tenants — those are business decisions
  the owner makes, not something to invent.
- Does not assume the automotive anchor's exact size/placement — flagged
  above as undecided.
- Does not change or supersede Phase 3's MVP scope.

## Suggested next concrete build step

Two options, either is a reasonable next script once picked:

1. **Extend the ground floor**: add one anchor-sized flagship bay
   (16–24m) past the existing 3 MVP bays, proving out the "Anchor store"
   unit from `MALL_LAYOUT.md` for the first time.
2. **Start Level 2**: add the vertical circulation (stairs/elevator
   greybox) in the atrium core and the Level 2 floor slab directly above
   the existing corridor, proving the "reuse the core, add a floor"
   principle for the first time.

Not started yet — pick one before a script gets written, to keep
building incremental and verifiable (screenshot-checked) like every
other Phase 3 step so far.
