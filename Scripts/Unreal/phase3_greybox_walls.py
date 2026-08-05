"""
Phase 3 Greybox — auto-place Atrium + corridor walls.

Run AFTER phase3_greybox_floors.py (uses the same coordinate system and
must stay in sync with Docs/Architecture/MALL_LAYOUT.md — do not change
numbers here without updating that doc too).

Requires: Python Editor Script Plugin enabled (see
phase3_greybox_floors.py for how). Run via:
  Tools > Execute Python Script... > select this file > Open.

Layout recap (all cm, 1 cm = 1 Unreal Unit):
  Atrium: 24m x 24m, centered at (0,0,0) -> spans X/Y -1200..1200
  Corridor: 36m long x 8m wide, centered at (3000,0,0) -> spans
            X 1200..4800, Y -400..400
  Wall height: 500cm (5m floor-to-floor, per MALL_LAYOUT.md)
  Wall thickness: 20cm

Openings (intentional, not missing walls):
  - Atrium south wall: 4m entrance gap, centered at X=0
  - Atrium east wall: 8m gap where the corridor connects (matches
    corridor width exactly)
  - Corridor far end (X=4800): left fully open — this is the
    removable-endcap expansion point per MALL_LAYOUT.md, not built yet
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
WALL_THICKNESS_CM = 20.0
WALL_Z_CENTER = WALL_HEIGHT_CM / 2.0  # sits on the floor (Z=0) up to Z=500


def spawn_wall(name, center_x_cm, center_y_cm, length_cm, along_x):
    """Spawns one wall segment. along_x=True means the wall runs along the
    X axis (so its long dimension is X, thin dimension is Y) — i.e. a
    north/south-facing wall. along_x=False is the reverse (east/west-facing)."""
    location = unreal.Vector(center_x_cm, center_y_cm, WALL_Z_CENTER)
    actor = editor_actor_subsystem.spawn_actor_from_object(cube_mesh, location)
    actor.set_actor_label(name)
    if along_x:
        scale = unreal.Vector(length_cm / 100.0, WALL_THICKNESS_CM / 100.0, WALL_HEIGHT_CM / 100.0)
    else:
        scale = unreal.Vector(WALL_THICKNESS_CM / 100.0, length_cm / 100.0, WALL_HEIGHT_CM / 100.0)
    actor.set_actor_scale3d(scale)
    return actor


# --- Atrium walls (24m x 24m, centered at origin, spans -1200..1200) ---

# North wall (full length, no opening).
spawn_wall("SM_AtriumWall_North_Greybox", center_x_cm=0, center_y_cm=1200, length_cm=2400, along_x=True)

# West wall (full length, no opening).
spawn_wall("SM_AtriumWall_West_Greybox", center_x_cm=-1200, center_y_cm=0, length_cm=2400, along_x=False)

# South wall — 4m entrance gap centered at X=0. Two segments of 10m each.
spawn_wall("SM_AtriumWall_South_A_Greybox", center_x_cm=-700, center_y_cm=-1200, length_cm=1000, along_x=True)
spawn_wall("SM_AtriumWall_South_B_Greybox", center_x_cm=700, center_y_cm=-1200, length_cm=1000, along_x=True)

# East wall — 8m corridor opening centered at Y=0 (matches corridor width).
# Two segments of 8m each.
spawn_wall("SM_AtriumWall_East_A_Greybox", center_x_cm=1200, center_y_cm=800, length_cm=800, along_x=False)
spawn_wall("SM_AtriumWall_East_B_Greybox", center_x_cm=1200, center_y_cm=-800, length_cm=800, along_x=False)

# --- Corridor walls (36m long, along X 1200..4800, Y = +/-400) ---

spawn_wall("SM_CorridorWall_North_Greybox", center_x_cm=3000, center_y_cm=400, length_cm=3600, along_x=True)
spawn_wall("SM_CorridorWall_South_Greybox", center_x_cm=3000, center_y_cm=-400, length_cm=3600, along_x=True)

unreal.EditorLevelLibrary.save_current_level()

print("Phase 3 greybox: 8 wall segments placed (atrium entrance + corridor opening left intentionally open) and level saved.")
print("Next: block out the first 3 store bays per Docs/Architecture/MALL_LAYOUT.md.")
