# Unreal Game Architecture — Mall Kit

Status: **planned, not yet implemented** — no `.uproject` exists yet (see
`Docs/Setup/UNREAL_SETUP.md`). This document defines the architecture to
build once it does.

## Core principle: modular, data-driven, not hardcoded maps

- Never build a store as a closed, hardcoded map.
- Build a **Mall Kit**: composable parts — walls, floors, ceilings,
  columns, storefront windows, doors, stairs, elevators, escalators,
  signage, lighting modules.
- Every store is **data-driven**, not hardcoded logic. See
  `Docs/Architecture/DATA_MODEL.md`.
- Every product loads from the Product data structure.
- Every store loads from a Store Configuration.
- Separate graphics, business data, and interaction logic.
- Use Blueprints for gameplay/interaction systems where appropriate.
- Use C++ only where it gives a real, concrete performance or
  architectural advantage.
- No unnecessary rewrites of working systems. Every component should be
  replaceable and extensible.

## Core systems to design

| System | Responsibility |
|---|---|
| Mall Game Mode | Top-level game rules/state for the mall experience |
| Player Controller | Input handling |
| First Person Character | Movement, camera |
| Interaction Component | Generic "can this actor be interacted with" logic |
| Product Actor | In-world representation of a `Product` |
| Store Manager | Loads a store from its `Store` config, spawns its contents |
| Mall Directory System | Store/zone lookup, map data |
| Navigation System | Wayfinding, signage, minimap |
| Shopping Cart System | Local cart state (mock checkout initially) |
| Product Information UI | The product detail card |
| Storefront Loading System | Streams/loads store content by proximity |
| Save System | Player position, settings |
| Audio Zone System | Per-zone ambient audio |
| NPC / AI Agent Interface | Lobby rep / per-store AI agent hook |
| Backend API Interface | Talks to the Supabase backend — see `Docs/Architecture/BACKEND_INTEGRATION.md` |
| Analytics Event System | Foot traffic / view / interaction events |

## Interaction flow

The user should be able to:

1. Approach a product.
2. See a clear prompt/highlight.
3. Press an interact key.
4. Open a product card.
5. Rotate/zoom the 3D product.
6. Read information.
7. Add to cart.
8. Move to the next product.
9. Close the card and keep walking.

Suggested Blueprint/Interface classes:
`BPI_Interactable`, `BP_InteractionComponent`, `BP_ProductActor`,
`WBP_InteractionPrompt`, `WBP_ProductDetails`, `BP_StoreTrigger`,
`BP_AutomaticDoor`.

## Store Template

A single reusable template that any store instance is built from — never
a bespoke map per store:

- Storefront facade
- Name and logo
- Entrance door
- Display area
- Shelves
- Product points
- Service counter
- Checkout
- Advertising area
- Background music
- Store-specific lighting
- NPC or service screen
- Exit back to the mall

The store is never tied to a specific product — content comes from a
Data Table / Data Asset / API (see `Docs/Architecture/DATA_MODEL.md` and
`Docs/Architecture/CONTENT_PIPELINE.md`).

## Folder structure (once the Unreal project exists)

Extends the existing `Content/CORE_AI/` convention
(`Docs/Architecture/UNREAL_STRUCTURE.md`) with game-specific structure:

```
Content/
  Mall/
    Architecture/
    Materials/
    Props/
    Lighting/
    Stores/
    Products/
    Navigation/
    Advertising/
  Core/
    Blueprints/
    Components/
    Interfaces/
    Data/
    UI/
    Save/
    Audio/
  Characters/
    Player/
    NPC/
  Maps/
    Development/
    Mall/
    Stores/
  Developer/
  Tests/

Source/
  ShayVirtualMall/
    Core/
    Interaction/
    Commerce/
    Navigation/
    AI/
    Data/
```

This sits alongside (not instead of) `Content/CORE_AI/` — `CORE_AI` is
where AI-generated/AI-managed content specifically lives (per
`CLAUDE.md` rule 4); the structure above is the general Unreal project
layout once real development starts, and AI-generated assets that
graduate from `CORE_AI/Generated/` land inside these folders.

## Performance targets

- MVP must run reasonably on a mid-range machine.
- Define Scalability Settings.
- Use Level Streaming or World Partition only as needed.
- Never render every store/product at full quality simultaneously.
- Use LOD, Nanite, occlusion, and zone-based loading.
- Document a performance budget per zone once real content exists.
