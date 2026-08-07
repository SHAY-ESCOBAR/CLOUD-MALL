"""
Phase 3 Greybox — ceiling over everything built so far (Atrium, corridor,
and the store row: Technology / Fashion / Cafe / Flagship Anchor).

Run AFTER phase3_greybox_floors.py, phase3_greybox_walls.py,
phase3_greybox_bays.py, and groundfloor_flagship_anchor.py. Requires:
Python Editor Script Plugin enabled. Run via:
  Tools > Execute Python Script... > select this file > Open.
Safe to re-run (destroys its own previously-placed actors by label first).

What this adds (all cm, 1 cm = 1 Unreal Unit):
  3 ceiling slabs, each sitting on top of the existing 500cm walls
  (bottom face at Z=500), mirroring the footprints already built rather
  than each individual floor piece, to keep the actor count low:
    - Atrium ceiling: 24m x 24m, centered at (0,0) - same footprint as
      SM_AtriumFloor_Greybox.
    - Corridor ceiling: one 48m x 8m slab spanning the corridor's full
      current extent (X 1200..6000) - covers both
      SM_MainCorridorFloor_Greybox and SM_CorridorFloorExtension_Greybox
      in one piece.
    - Store row ceiling: one 48m x 12m slab spanning X 1200..6000 at
      Y 400..1600 - covers all 4 store bays (3 MVP bays + the Flagship
      Anchor) in one piece, since they're contiguous.

IMPORTANT — this does NOT extend to future expansion:
  If/when the corridor or store row grows past X=6000 (per
  MALL_LAYOUT.md's "removable endcap" principle), this ceiling will need
  a matching extension - it won't magically cover new area. Re-run this
  script after any expansion.

IMPORTANT — this will conflict with Level 2 if/when that gets built:
  TENANT_MIX_PLAN.md's option 2 (Level 2 boutique floor) would sit right
  where this ceiling is (Z=500 and up). Building Level 2 later means this
  ceiling's slabs need to become that floor, not stay as a solid roof.
  Documented here so it isn't a surprise later - not a problem to solve
  now.

What this does NOT do:
  - Does not add any lighting fixtures (the existing DirectionalLight/
    SkyLight are outside now that there's a ceiling - interior lighting
    becomes a real Phase 3 follow-up, not handled by this script).
  - Does not cut any openings (skylights, vents) into the ceiling.
"""

import unreal

editor_actor_subsystem = unreal.get_editor_subsystem(unreal.EditorActorSubsystem)
cube_mesh = unreal.EditorAssetLibrary.load_asset("/Engine/BasicShapes/Cube.Cube")

if cube_mesh is None:
    raise RuntimeError(
        "Could not load /Engine/BasicShapes/Cube.Cube — enable 'Show Engine "
        "Content' in the Content Browser view options and try again."
    )

WALL_HEIGHT_CM = 500.0
CEILING_THICKNESS_CM = 20.0
CEILING_Z_CENTER = WALL_HEIGHT_CM + CEILING_THICKNESS_CM / 2.0  # bottom face sits at Z=500


def spawn_ceiling_slab(name, location_cm, footprint_m_xy, thickness_cm=CEILING_THICKNESS_CM):
    location = unreal.Vector(location_cm[0], location_cm[1], location_cm[2])
    actor = editor_actor_subsystem.spawn_actor_from_object(cube_mesh, location)
    actor.set_actor_label(name)
    scale_x = footprint_m_xy[0] * 100.0 / 100.0
    scale_y = footprint_m_xy[1] * 100.0 / 100.0
    scale_z = thickness_cm / 100.0
    actor.set_actor_scale3d(unreal.Vector(scale_x, scale_y, scale_z))
    return actor


def destroy_actor_by_label(label):
    for actor in editor_actor_subsystem.get_all_level_actors():
        if actor.get_actor_label() == label:
            editor_actor_subsystem.destroy_actor(actor)
            return True
    return False


for label in [
    "SM_AtriumCeiling_Greybox",
    "SM_CorridorCeiling_Greybox",
    "SM_StoreRowCeiling_Greybox",
]:
    destroy_actor_by_label(label)

# Atrium ceiling: matches SM_AtriumFloor_Greybox footprint (24m x 24m at origin).
spawn_ceiling_slab(
    name="SM_AtriumCeiling_Greybox",
    location_cm=(0.0, 0.0, CEILING_Z_CENTER),
    footprint_m_xy=(24.0, 24.0),
)

# Corridor ceiling: full current extent, X 1200..6000 (48m), 8m wide, centered at X=3600.
spawn_ceiling_slab(
    name="SM_CorridorCeiling_Greybox",
    location_cm=(3600.0, 0.0, CEILING_Z_CENTER),
    footprint_m_xy=(48.0, 8.0),
)

# Store row ceiling: X 1200..6000 (48m), 12m deep, Y 400..1600 -> center Y=1000.
spawn_ceiling_slab(
    name="SM_StoreRowCeiling_Greybox",
    location_cm=(3600.0, 1000.0, CEILING_Z_CENTER),
    footprint_m_xy=(48.0, 12.0),
)

unreal.EditorLevelLibrary.save_current_level()

print("Phase 3 greybox: ceiling placed over Atrium + corridor + store row (3 slabs) and level saved.")
print("Known follow-up: no interior lighting yet (existing lights are now outside the ceiling), no openings cut, and this will need extending or replacing if the corridor/store row grows or Level 2 gets built - see this script's docstring.")
