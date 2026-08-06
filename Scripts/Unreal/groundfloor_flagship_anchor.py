"""
Ground Floor Expansion — first Flagship Anchor store.

Beyond Phase 3's original MVP scope (Atrium + 3 bays) — this is the first
concrete build step from Docs/Architecture/TENANT_MIX_PLAN.md ("Suggested
next concrete build step", option 1), explicitly requested next. Run
AFTER phase3_greybox_floors.py, phase3_greybox_walls.py, and
phase3_greybox_bays.py.

Requires: Python Editor Script Plugin enabled. Run via:
  Tools > Execute Python Script... > select this file > Open.
Safe to re-run (destroys its own previously-placed actors by label first).

What this adds (all cm, 1 cm = 1 Unreal Unit):
  - One Flagship Anchor store bay, 24m wide x 12m deep — the MAX size in
    MALL_LAYOUT.md's "Anchor store: 2-3 bay modules wide (16-24m)" range,
    picked because the brief was "big brand flagship stores"
    (TENANT_MIX_PLAN.md ground floor). If 24m ends up too large next to
    the existing 8m-wide inline bays, this is a one-number change
    (ANCHOR_WIDTH_CM below) and a re-run.
  - Placed immediately east of the existing Cafe bay (shares Cafe's
    existing east wall as its own west wall - no new divider needed
    there), open frontage onto the corridor, same as the other 3 bays.
  - Extends the corridor (floor + south wall) from X=4800 (old end) to
    X=6000, since the corridor wasn't long enough to reach a 24m anchor.
  - A temporary east endcap wall at X=6000 - same "removable endcap, not
    a permanent wall" concept MALL_LAYOUT.md already uses for the
    corridor's far end; remove this when the next expansion continues
    east.

What this REMOVES and why:
  - SM_CorridorWall_North_Remainder_Greybox (the solid X 3600..4800
    stretch phase3_greybox_bays.py added for "not built yet"). That
    stretch is now the Flagship Anchor's storefront frontage, so it must
    be open, not solid. Removed by label - it's our own greybox
    placeholder, not user content.

What this does NOT do:
  - Does not name a real brand/tenant - that's a business decision, not
    invented here.
  - Does not touch the south side of the corridor beyond X=6000, or Level
    2 - those stay open/unbuilt, per TENANT_MIX_PLAN.md.
  - Does not touch Supabase / mall_units - this is geometry only.
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
WALL_Z_CENTER = WALL_HEIGHT_CM / 2.0
FLOOR_THICKNESS_CM = 20.0

# Existing geometry this script extends (do not change without checking
# phase3_greybox_walls.py / phase3_greybox_bays.py stay in sync):
OLD_CORRIDOR_END_X = 4800.0   # where the corridor floor/south wall used to stop
CAFE_EAST_X = 3600.0          # Cafe bay's existing east wall — becomes the anchor's west wall
CORRIDOR_Y_NORTH = 400.0      # corridor north wall line (bay frontage line)
CORRIDOR_Y_SOUTH = -400.0

ANCHOR_WIDTH_CM = 2400.0      # 24m — top of MALL_LAYOUT.md's 16-24m anchor range
ANCHOR_Y_FRONT = 400.0
ANCHOR_Y_BACK = 1600.0        # same 12m depth as the other 3 bays
ANCHOR_Y_CENTER = (ANCHOR_Y_FRONT + ANCHOR_Y_BACK) / 2.0

ANCHOR_X_MIN = CAFE_EAST_X                       # 3600
ANCHOR_X_MAX = CAFE_EAST_X + ANCHOR_WIDTH_CM      # 6000
ANCHOR_X_CENTER = (ANCHOR_X_MIN + ANCHOR_X_MAX) / 2.0

NEW_CORRIDOR_END_X = ANCHOR_X_MAX  # corridor now needs to reach 6000


def spawn_floor_slab(name, location_cm, footprint_m_xy, thickness_cm=FLOOR_THICKNESS_CM):
    location = unreal.Vector(location_cm[0], location_cm[1], location_cm[2])
    actor = editor_actor_subsystem.spawn_actor_from_object(cube_mesh, location)
    actor.set_actor_label(name)
    scale_x = footprint_m_xy[0] * 100.0 / 100.0
    scale_y = footprint_m_xy[1] * 100.0 / 100.0
    scale_z = thickness_cm / 100.0
    actor.set_actor_scale3d(unreal.Vector(scale_x, scale_y, scale_z))
    return actor


def spawn_wall(name, center_x_cm, center_y_cm, length_cm, along_x):
    location = unreal.Vector(center_x_cm, center_y_cm, WALL_Z_CENTER)
    actor = editor_actor_subsystem.spawn_actor_from_object(cube_mesh, location)
    actor.set_actor_label(name)
    if along_x:
        scale = unreal.Vector(length_cm / 100.0, WALL_THICKNESS_CM / 100.0, WALL_HEIGHT_CM / 100.0)
    else:
        scale = unreal.Vector(WALL_THICKNESS_CM / 100.0, length_cm / 100.0, WALL_HEIGHT_CM / 100.0)
    actor.set_actor_scale3d(scale)
    return actor


def destroy_actor_by_label(label):
    for actor in editor_actor_subsystem.get_all_level_actors():
        if actor.get_actor_label() == label:
            editor_actor_subsystem.destroy_actor(actor)
            return True
    return False


# --- Step 1: remove the old "not built yet" wall — this stretch is now the anchor's frontage ---

removed = destroy_actor_by_label("SM_CorridorWall_North_Remainder_Greybox")
print(
    "Removed old SM_CorridorWall_North_Remainder_Greybox (was blocking the anchor's frontage)."
    if removed else
    "SM_CorridorWall_North_Remainder_Greybox not found (already removed or bays script not run yet) — continuing."
)
# Also safe to re-run this whole script:
destroy_actor_by_label("SM_CorridorFloorExtension_Greybox")
destroy_actor_by_label("SM_CorridorWall_South_Extension_Greybox")
destroy_actor_by_label("SM_FlagshipAnchorFloor_Greybox")
destroy_actor_by_label("SM_FlagshipAnchorWall_Back_Greybox")
destroy_actor_by_label("SM_FlagshipAnchorWall_East_Greybox")

# --- Step 2: extend the corridor from X=4800 to X=6000 so it reaches the anchor ---

corridor_ext_length = NEW_CORRIDOR_END_X - OLD_CORRIDOR_END_X  # 1200 (12m)
corridor_ext_center_x = OLD_CORRIDOR_END_X + corridor_ext_length / 2.0  # 5400

spawn_floor_slab(
    name="SM_CorridorFloorExtension_Greybox",
    location_cm=(corridor_ext_center_x, 0.0, 0.0),
    footprint_m_xy=(corridor_ext_length / 100.0, 8.0),
)
spawn_wall(
    "SM_CorridorWall_South_Extension_Greybox",
    center_x_cm=corridor_ext_center_x, center_y_cm=CORRIDOR_Y_SOUTH,
    length_cm=corridor_ext_length, along_x=True,
)
# North side of this stretch is left fully open — it's the anchor's frontage.

# --- Step 3: the Flagship Anchor bay itself (24m x 12m) ---

spawn_floor_slab(
    name="SM_FlagshipAnchorFloor_Greybox",
    location_cm=(ANCHOR_X_CENTER, ANCHOR_Y_CENTER, 0.0),
    footprint_m_xy=(ANCHOR_WIDTH_CM / 100.0, 12.0),
)
spawn_wall(
    "SM_FlagshipAnchorWall_Back_Greybox",
    center_x_cm=ANCHOR_X_CENTER, center_y_cm=ANCHOR_Y_BACK,
    length_cm=ANCHOR_WIDTH_CM, along_x=True,
)
# West wall: reuses the existing SM_BayWall_CafeEast_Greybox — not respawned here.
# East wall: temporary endcap (removable, matches MALL_LAYOUT.md's endcap concept).
spawn_wall(
    "SM_FlagshipAnchorWall_East_Greybox",
    center_x_cm=ANCHOR_X_MAX, center_y_cm=ANCHOR_Y_CENTER,
    length_cm=(ANCHOR_Y_BACK - ANCHOR_Y_FRONT), along_x=False,
)

unreal.EditorLevelLibrary.save_current_level()

print("Ground floor expansion: 1 Flagship Anchor bay (24m x 12m) placed east of Cafe, corridor extended to X=6000, and level saved.")
print("Known follow-up (not done by this script): storefront wall/glass/door, ceiling, brand/tenant assignment, and TENANT_MIX_PLAN.md option 2 (Level 2) still not started.")
