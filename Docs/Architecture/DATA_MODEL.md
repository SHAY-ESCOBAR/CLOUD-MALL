# Data Model

Status: **planned**. This defines the target data shapes for
Unreal-side Data Assets/Data Tables, and how they map onto the backend
that already exists (`Docs/Architecture/BACKEND_INTEGRATION.md`).

## Principle

Everything is data-driven. No product or store is hardcoded into a
Blueprint or a map. Content loads from a Data Table, Data Asset, or the
backend API.

## Product

| Field | Notes |
|---|---|
| id | |
| sku | |
| name | |
| category | |
| description | |
| price | |
| currency | |
| stock | |
| image | |
| model_3d | Path/URL to the 3D asset (once product-level 3D models exist) |
| video | |
| brand | |
| tags | |
| store_id | |
| interaction_type | e.g. inspect / try-on / add-to-cart |
| purchase_url | |

**Existing backend mapping:** this corresponds closely to the `products`
table already in Supabase (`name`, `description`, `price`, `image_url`,
`category`, `sku`, `in_stock`, `ar_model_url`). `ar_model_url` is the
natural fit for `model_3d`. Field names differ slightly (`in_stock` vs.
`stock`, `image_url` vs. `image`) — reconcile when the Unreal client
actually queries this table, rather than assuming a 1:1 rename now.

## Store

| Field | Notes |
|---|---|
| id | |
| name | |
| category | |
| logo | |
| description | |
| location | |
| opening_hours | |
| products | |
| theme | |
| music | |
| npc_agent | |
| promotions | |

**Existing backend mapping:** `mall_units` already has `unit_code`,
`floor`, `zone`, `display_name`, `description`, `area_sqm`,
`monthly_rate_ils`/`setup_fee_ils` (real-money fields — see the safety
rules in `Docs/Architecture/BACKEND_INTEGRATION.md`), `is_anchor`,
`metadata` (JSONB — already used for `emoji`/`route`/`live` in the
10-store seed migration in `cyber-solar-nexus`). `mall_leases` is the
tenant/rent relationship on top of a unit. A Store (game-side) generally
corresponds to a leased, active `mall_unit`.

## Mall

| Field | Notes |
|---|---|
| id | |
| name | |
| floors | |
| zones | |
| stores | |
| entrances | |
| navigation_points | |
| advertising_spaces | |
| event_spaces | |

**Existing backend mapping:** `floors` and `zones` already exist as
Postgres enums on `mall_units` (`mall_floor`: `ground`/`level_2`/`level_3`;
`mall_zone`: `market`/`kiosk`/`fashion_anchor`/`fashion_inline`/
`tech_arena`/`social_zone`). No dedicated "garden/social" zone exists yet
for content like the `cyber-solar-nexus` "Garden Walk" section — either
add a zone value or fold it into `social_zone` (open decision, not yet
made — do not assume one silently when this is implemented).

## Where this data actually lives (near-term)

Until the Unreal ↔ Supabase integration is built
(`Docs/Architecture/BACKEND_INTEGRATION.md`, Phase 7 in `ROADMAP.md`),
early greybox/MVP work should use **local Unreal Data Assets/Data Tables**
seeded by hand or exported from the same source data used to seed
`mall_units` (see the 10-store seed migration in `cyber-solar-nexus`), not
a live network call. Wire the real API only once the read-only
integration milestone is reached.
