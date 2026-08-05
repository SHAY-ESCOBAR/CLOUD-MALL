"""
Phase 3 Greybox — auto-place the Atrium and main corridor floor slabs.

Dimensions come from Docs/Architecture/MALL_LAYOUT.md — do not change the
numbers here without updating that doc too, they must stay in sync.

Requires: Python Editor Script Plugin enabled
(Edit > Plugins > search "Python Editor Script Plugin" > enable > restart
the Editor). This is unverified as of ROADMAP.md Phase 0 — if this script
fails to run at all, that plugin is almost certainly the reason.

How to run this (no typing/pasting code required):
  Tools > Execute Python Script...  (or Window > Execute Python Script,
  depending on Unreal version) > browse to this file > Open.

What it does:
  - Spawns two StaticMeshActors using the Engine's default Cube mesh,
    scaled into thin floor slabs, at real-world scale (1 cm = 1 Unreal
    Unit).
  - Names them descriptively (never "Cube1"/"NewBlueprint" — CLAUDE.md
    rule 5).
  - Saves the current level afterward.

What it does NOT do:
  - Does not add walls, ceilings, columns, or store bays yet — this is
    step one (floors only), to confirm scale/placement before adding
    more.
  - Does not touch any file outside the current open level.
"""

import unreal

editor_actor_subsystem = unreal.get_editor_subsystem(unreal.EditorActorSubsystem)
cube_mesh = unreal.EditorAssetLibrary.load_asset("/Engine/BasicShapes/Cube.Cube")

if cube_mesh is None:
    raise RuntimeError(
        "Could not load /Engine/BasicShapes/Cube.Cube — the Engine Content "
        "basic shapes may not be visible. Enable 'Show Engine Content' in "
        "the Content Browser view options and try again."
    )


def spawn_floor_slab(name, location_cm, footprint_m_xy, thickness_cm=20.0):
    """Spawns a thin floor slab. footprint_m_xy is (width_m, depth_m)."""
    location = unreal.Vector(location_cm[0], location_cm[1], location_cm[2])
    actor = editor_actor_subsystem.spawn_actor_from_object(cube_mesh, location)
    actor.set_actor_label(name)
    # Engine's default Cube is 100x100x100 cm at scale (1,1,1).
    scale_x = footprint_m_xy[0] * 100.0 / 100.0  # meters -> cm -> cube units
    scale_y = footprint_m_xy[1] * 100.0 / 100.0
    scale_z = thickness_cm / 100.0
    actor.set_actor_scale3d(unreal.Vector(scale_x, scale_y, scale_z))
    return actor


# Atrium floor: 24m x 24m, centered at the world origin.
spawn_floor_slab(
    name="SM_AtriumFloor_Greybox",
    location_cm=(0.0, 0.0, 0.0),
    footprint_m_xy=(24.0, 24.0),
)

# Main corridor floor: 8m wide x 36m long (first 3 bay modules' worth),
# extending out from the atrium's edge along +X.
# Atrium half-width = 12m = 1200cm, so the corridor starts at X=1200cm.
# Corridor center X = 1200 + (3600 / 2) = 3000cm.
spawn_floor_slab(
    name="SM_MainCorridorFloor_Greybox",
    location_cm=(3000.0, 0.0, 0.0),
    footprint_m_xy=(36.0, 8.0),
)

unreal.EditorLevelLibrary.save_current_level()

print("Phase 3 greybox: Atrium floor + main corridor floor placed and level saved.")
print("Next: review in the Editor, then add walls/bays per Docs/Architecture/MALL_LAYOUT.md.")
