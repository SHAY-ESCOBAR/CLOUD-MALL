# Backend Integration — Reusing the `cyber-solar-nexus` Supabase Project

## Decision

CLOUD MALL's Unreal Engine 5 client will **connect to the existing
Supabase backend already built for `cyber-solar-nexus`**, instead of
choosing/building a new purchase backend from scratch. That repository is
a Lovable-originated web app (React + Vite + `react-three-fiber`) that
already implements a browser-based 3D mall with real cart/wallet/store
logic on top of this Supabase project.

This was an explicit owner decision (2026-08-05), made after discovering
`cyber-solar-nexus` already has a working mall data model — see below.
It significantly changes Phase 7 of `ROADMAP.md`: instead of "choose a
backend," the work becomes "integrate Unreal with an existing one."

## What already exists (as of this writing)

Supabase project ref: `qubbzwbtvuvpbcaasjmz` (from
`cyber-solar-nexus/supabase/config.toml` — this is a project identifier,
**not a secret**, but no keys are recorded here either; see Safety below).

Known tables (from `cyber-solar-nexus/supabase/migrations/`), all with Row
Level Security enabled:

| Table | Purpose |
|---|---|
| `store_scenes` | Saved/generated store designs, with `anchor_points` (JSONB) marking where products sit in a scene, `store_style`, `is_published` |
| `products` | Product catalog: name, description, price, image_url, category, sku, in_stock, **ar_model_url** (already anticipates AR/3D models per product) |
| `anchor_assignments` | Links a product to a specific anchor point within a scene |
| `user_roles` | `admin` / `moderator` / `user` roles, via a `has_role()` security-definer function |
| `admin_analytics` | Event tracking, optionally tied to a scene |
| `global_settings` | Key/value config (theme override, resolution mode, environment modifiers) |
| `mall_units` | **120 leasable units** — floor (`ground`/`level_2`/`level_3`), zone (`market`/`kiosk`/`fashion_anchor`/`fashion_inline`/`tech_arena`/`social_zone`), area in sqm, monthly/setup rate **in ILS (₪)** |
| `mall_leases` | Tenant leases against `mall_units`, with status (`available`/`reserved`/`active`/`expired`), linked to a `store_scenes` row |

Storage: a public `product-images` bucket with per-user-folder RLS.

This is a real, structured mall-leasing and e-commerce data model — not a
mockup. `mall_units`/`mall_leases` in particular model actual real-money
tenant relationships (rent in ILS).

## What this means for CLOUD MALL's architecture

```
Unreal Engine 5 Client (3D mall, native)
      |
      | HTTPS (Supabase REST/PostgREST, or a thin API layer)
      v
Supabase project qubbzwbtvuvpbcaasjmz
      |
      +-- products / store_scenes / anchor_assignments  (catalog + AR/3D placement)
      +-- mall_units / mall_leases                        (which stores exist, where, real ILS rent)
      +-- user_roles / admin_analytics / global_settings   (admin + ops)
```

Practical implications:

- Unreal's blockout/production mall layout should ultimately be able to
  read `mall_units` (floor/zone/position) so the **3D layout and the real
  leasing data agree** — a unit's in-world position and its DB row should
  reference the same `unit_code`.
- `anchor_points` in `store_scenes` (JSONB) already encodes where a
  product sits in a scene for the web/AR version. The Unreal equivalent
  (an anchor Actor/Blueprint tied to a `product_id`) should be designed to
  read from the same `anchor_assignments` table, not a parallel one.
- Authentication/roles (`user_roles`, `has_role()`) already exist — Unreal
  should authenticate against the same Supabase Auth rather than building
  a separate login system.

## How Unreal will call this (to be implemented)

Not yet built. Options to evaluate when this work starts:

1. **Direct Supabase REST (PostgREST) calls from Unreal**, using Unreal's
   HTTP module, with a Supabase **anon** key scoped by RLS policies.
2. **A thin intermediary API** (e.g. a Supabase Edge Function) that the
   Unreal client calls instead of hitting PostgREST directly — gives more
   control over what native clients can do versus the web app.

Either way: **no admin/service-role key is ever embedded in the Unreal
client** — only the public anon key, relying on RLS (same model the web
app already uses).

## Safety rules specific to this integration

- Never commit a Supabase service-role key, DB password, or JWT secret to
  this repository (or to `cyber-solar-nexus`). Only the public anon key
  may ever appear in client-side config, and even that belongs in an
  Unreal `Config/` `.ini` that is reviewed before commit, not hardcoded in
  Blueprints.
- `mall_leases` and `mall_units` represent real tenant/rent relationships.
  Do not write to these tables from AI-driven Unreal/MCP automation
  without the same explicit approval gate defined in `CLAUDE.md` rule 12
  for real purchases — leasing a unit is a real-money action, same class
  of risk as checkout.
- Read-only integration (browsing the catalog, rendering mall layout from
  `mall_units`) is safe to build first. Any write path (creating a lease,
  modifying `products`, changing `global_settings`) needs the same
  separate-approval treatment as Phase 7 payment integration.
- `cyber-solar-nexus`'s `.env` file was previously flagged as tracked in
  that repository (see its `README.md` security note) — rotate any
  credentials there before relying on this Supabase project for anything
  beyond local development.
