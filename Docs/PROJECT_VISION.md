# Project Vision — Shay Virtual Mall

## What this is

A digital, interactive, modular 3D mall built in Unreal Engine 5, where
users can move freely, enter stores, view products, get information, talk
to AI agents, watch content, and — eventually — perform real purchases and
actions.

This is **not just a game** and **not just an e-commerce site**. It is a
living commercial world connecting:

- Unreal Engine (native 3D experience)
- First-person navigation
- Virtual stores
- Real and digital products
- AI systems (product-aware agents)
- Databases (see `Docs/Architecture/BACKEND_INTEGRATION.md` — the existing
  Supabase project from `cyber-solar-nexus`)
- User accounts
- Inventory and pricing
- Future payment systems
- Advertising and brand experiences
- Events, community, entertainment

## The real product

The mall itself (`SHAY MALL — FUTURE DISTRICT`, the first showcase build)
is not the end goal. The actual product is:

> **A system that generates and operates 3D malls and stores for
> businesses.**

Each store a tenant gets:
- Its own 3D space.
- An AI agent that knows its products.
- Physical and digital products.
- Video displays, launch events, private rooms.
- User-targeted promotions.
- The ability to change the store's content without rebuilding Unreal.
- A business-owner dashboard.
- Analytics on foot traffic, views, and interactions.

## Visual reference

Photorealistic environment in the style of a modern mall / first-person
game. The user enters a central structure, moves through corridors, sees
storefronts, enters different stores, examines shelves and products, and
triggers interactive points.

## Relationship to what already exists

- **`cyber-solar-nexus`** (sibling repo) is a working browser-based
  version of this same idea (panorama-based navigation, real Supabase
  backend with `mall_units`/`mall_leases`/`products`). It is the fastest
  path to something live today, and its Supabase project is the intended
  shared backend for the native Unreal client (see
  `Docs/Architecture/BACKEND_INTEGRATION.md`).
- **This repo (`CLOUD-MALL`)** is where the **native, Unreal Engine 5**
  version — the one described in this document — is built. Internally the
  Unreal project itself may be named `ShayVirtualMall`; the GitHub
  repository stays `CLOUD-MALL` so the project isn't fragmented across
  yet another repo (see `Docs/Decisions/ADR-002-SHAY-VIRTUAL-MALL-SCOPE.md`).

## Opening build: SHAY MALL — FUTURE DISTRICT

Not 100 stores. One impressive district, enough to demo the vision to
investors, businesses, partners, and developers — not just describe it in
words:

1. Central entrance hall.
2. One fully active technology store.
3. A showroom for CORE systems and your automotive projects.
4. A digital café.
5. One closed store with "Coming Soon" signage (proves extensibility).
6. An AI representative in the lobby.
7. A large screen showing projects, ads, and events.
8. A transition area that visually implies the mall can keep expanding.

See `ROADMAP.md` for how this breaks down into buildable phases, and
`Docs/TASKS.md` for the current concrete task list.
