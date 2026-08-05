# Mall Layout — Expandable Modular Grid

Status: **design, not yet built in Unreal**. This is the spatial plan for
Phase 3 (Greybox) in `ROADMAP.md`, designed so the mall can always grow —
more stores, more floors, more wings — without reworking what already
exists.

## Core principle

Nothing about the layout should ever require touching existing geometry
to expand it. Every extension point (end of a corridor, top of an atrium)
is a swappable module, not a permanent wall or fixed size.

## The grid

Real-world scale throughout: **1 cm = 1 Unreal Unit** (per
`Docs/Architecture/UNREAL_STRUCTURE.md`).

| Element | Size |
|---|---|
| Base bay module (one inline store slot) | 8 m wide × 12 m deep |
| Anchor store | 2–3 bay modules wide (16–24 m) |
| Kiosk | 3 m × 3 m footprint, placed **inside** the corridor, not a bay |
| Corridor width | 8 m (double-loaded, stores both sides) |
| Floor-to-floor height | 5 m |
| Atrium (central hub) | 24 m × 24 m, houses vertical circulation core |

## Layout

```
                    +-------------+
                    |   ATRIUM    |  <- stairs + elevator + escalator core,
                    |  24m x 24m  |     sized now for future floors
                    +------+------+
                           |
   +----+----+----+----+--+-+----+----+----+-----  (extends this way)
   | B1 | B2 | B3 | B4 |CORR| B5 | B6 | ...       |
   |8x12|8x12|8x12|8x12| 8m |8x12|8x12|            |
   +----+----+----+----+----+----+----+------------+
     ^ MVP: only B1-B3 built                          ^ removable endcap,
       (technology / fashion / cafe)                    not a permanent wall
```

- The corridor spine extends indefinitely from the atrium by adding bay
  modules; the far end is capped with a removable endcap prop, never a
  structural wall.
- The atrium is a junction, not a dead end — a second corridor can later
  extend perpendicular from it (T or + shaped mall), because nothing is
  built assuming the atrium only has one exit.
- Additional floors reuse the same grid at
  `Z = floor_index * 500 cm` above the atrium's vertical core. Ground
  floor (Phase 3) is the only floor actually built; the core is sized for
  `level_2`/`level_3` from day one so adding them later doesn't require
  rebuilding the atrium.

## Mapping to the existing data model

Each bay gets a `unit_code` in the same scheme already used to seed
`mall_units` in Supabase (`Docs/Architecture/BACKEND_INTEGRATION.md`):
`<floor>-<zone>-<number>`, e.g. `G-M-01`. Bay position in the grid is the
physical counterpart of that row — B1/B2/B3 in the MVP correspond to 3 of
the 10 already-seeded stores (pick specific ones when blockout starts;
not decided yet — don't assume which 3 without confirming).

Zone placement along the spine, loosely following the existing
`cyber-solar-nexus` section ordering (`market → fashion → tech →
social_zone`) so the two versions stay conceptually aligned:

| Corridor position | Zone (matches `mall_zone` enum) |
|---|---|
| Near atrium | `market` / `kiosk` |
| Next | `fashion_anchor` / `fashion_inline` |
| Next | `tech_arena` |
| Further out | `social_zone` |

## MVP scope (Phase 3)

Only: Atrium + B1, B2, B3 (technology / fashion / café — per
`Docs/PROJECT_VISION.md`'s opening build), main corridor between them, one
entrance. Everything else in this document is the plan the MVP must not
contradict, not something to build yet.

## Visual style reference (inspiration only — not a licensed/imported asset)

Owner shared screenshots (2026-08-06) of a third-party Unreal Marketplace
demo scene ("ShoppingMall", running on UE 4.27 — a different engine
version than this project's 5.8, and not something being purchased or
imported) as **visual/style inspiration only**:

- Glass-facade exterior with a covered entrance canopy, branded signage
  ("PANORAMA CITY MALL" in the reference), palm trees / street furniture
  outside.
- Interior atrium: bright, warm-toned stone flooring, potted plants as
  atrium dividers, soft bench seating, visible second-floor storefronts
  and an escalator connecting floors — i.e. exactly the atrium-with-
  visible-upper-floor massing this layout's `24m × 24m` atrium + vertical
  core is designed to support.
- Branded storefront signage style (bold logo + lit signage above the
  glass shopfront) is a reasonable material/lighting target for Phase 7,
  not something to attempt during greybox.

This informs **materials, lighting, and dressing** in Phase 7
(`Docs/Architecture/CONTENT_PIPELINE.md`) — it does not change the Phase 3
greybox grid above, and no assets from that reference are used directly
(license unknown/unverified — see `CLAUDE.md` rule against unlicensed
commercial assets).
