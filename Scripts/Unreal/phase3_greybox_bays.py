"""
Phase 3 Greybox — auto-place the first 3 store bays (technology / fashion /
café) along the north side of the main corridor.

Run AFTER phase3_greybox_floors.py and phase3_greybox_walls.py. Uses the
same coordinate system and must stay in sync with
Docs/Architecture/MALL_LAYOUT.md — do not change numbers here without
updating that doc too.

Requires: Python Editor Script Plugin enabled (see phase3_greybox_floors.py
for how). Run via: Tools > Execute Python Script... > select this file >
Open.

Layout recap (all cm, 1 cm = 1 Unreal Unit):
  Corridor: spans X 1200..4800, Y -400..400 (built by
            phase3_greybox_walls.py, north wall at Y=400, south wall at
            Y=-400, both currently solid/unbroken).
  Bay module: 8m wide (X) x 12m deep (Y), per MALL_LAYOUT.md.

MVP scope (per MALL_LAYOUT.md "MVP scope (Phase 3)"): only 3 bays, all on
the corridor's NORTH side (Y > 400), placed back-to-back starting right
next to the atrium:
  Bay 1 - Technology : X 1200..2000
  Bay 2 - Fashion    : X 2000..2800
  Bay 3 - Cafe       : X 2800..3600
  (X 3600..4800 stays unbuilt — future bays, per the "removable endcap,
  not a permanent wall" principle in MALL_LAYOUT.md.)

Which real mall_units rows these 3 physical bays correspond to is NOT
decided yet (MALL_LAYOUT.md says so explicitly) — this script only builds
geometry, it does not touch Supabase or assign unit_codes.

IMPORTANT — fixes a conflict with the previous script's output:
  phase3_greybox_walls.py built SM_CorridorWall_North_Greybox as ONE solid
  36m wall with no gaps. That fully blocks these 3 storefronts from the
  corridor. This script deletes that one actor (by label — it's a greybox
  actor our own automation placed, not user content) and replaces it with
  a shorter wall that only covers the still-unbuilt X 3600..4800 stretch,
  leaving X 1200..3600 open as the 3 storefront frontages. The south
  corridor wall is untouched.

What this script does NOT do:
  - Does not add a storefront-facing wall/glass/door for each bay (open
    frontage only, for now).
  - Does not add a ceiling.
  - Does not decide which Supabase mall_units row maps to which bay.
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

BAY_Y_FRONT = 400.0   # corridor wall line (matches SM_CorridorWall_North_Greybox)
BAY_Y_BACK = 1600.0   # 12m deep
BAY_Y_CENTER = (BAY_Y_FRONT + BAY_Y_BACK) / 2.0


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
    """Finds a level actor by its exact label and destroys it. Returns True
    if something was found and destroyed, False otherwise (does not error
    if it's already gone, so this script is safe to re-run)."""
    for actor in editor_actor_subsystem.get_all_level_actors():
        if actor.get_actor_label() == label:
            editor_actor_subsystem.destroy_actor(actor)
            return True
    return False


# --- Step 1: fix the corridor's north wall so the 3 bays can open onto it ---

removed = destroy_actor_by_label("SM_CorridorWall_North_Greybox")
if removed:
    print("Removed old solid SM_CorridorWall_North_Greybox (36m, no gaps) — replacing with a shorter wall that leaves the 3 bay frontages open.")
else:
    print("SM_CorridorWall_North_Greybox not found (already removed or walls script not run yet) — continuing.")

# Remaining solid stretch beyond the 3 MVP bays: X 3600..4800 (12m).
spawn_wall(
    "SM_CorridorWall_North_Remainder_Greybox",
    center_x_cm=4200, center_y_cm=BAY_Y_FRONT, length_cm=1200, along_x=True,
)

# --- Step 2: the 3 bays (floor + back wall + shared dividers, open front) ---

BAYS = [
    {"key": "Technology", "x_min": 1200.0, "x_max": 2000.0},
    {"key": "Fashion", "x_min": 2000.0, "x_max": 2800.0},
    {"key": "Cafe", "x_min": 2800.0, "x_max": 3600.0},
]

for bay in BAYS:
    x_center = (bay["x_min"] + bay["x_max"]) / 2.0
    spawn_floor_slab(
        name="SM_Bay{}Floor_Greybox".format(bay["key"]),
        location_cm=(x_center, BAY_Y_CENTER, 0.0),
        footprint_m_xy=(8.0, 12.0),
    )

# One continuous back wall behind all 3 bays (X 1200..3600 at Y=1600).
spawn_wall(
    "SM_BayWall_TechFashionCafeBack_Greybox",
    center_x_cm=2400, center_y_cm=BAY_Y_BACK, length_cm=2400, along_x=True,
)

# Dividers between bays (shared walls, so 2 dividers for 3 bays — not 4,
# to avoid overlapping duplicate geometry). No wall at X=1200 (Technology's
# west edge, open toward the atrium/corridor junction) or X=3600 beyond
# Cafe other than the remainder wall above, which does not extend south
# into the bay depth — that boundary is intentionally left open for now.
spawn_wall(
    "SM_BayDivider_TechnologyFashion_Greybox",
    center_x_cm=2000, center_y_cm=BAY_Y_CENTER, length_cm=(BAY_Y_BACK - BAY_Y_FRONT), along_x=False,
)
spawn_wall(
    "SM_BayDivider_FashionCafe_Greybox",
    center_x_cm=2800, center_y_cm=BAY_Y_CENTER, length_cm=(BAY_Y_BACK - BAY_Y_FRONT), along_x=False,
)
spawn_wall(
    "SM_BayWall_CafeEast_Greybox",
    center_x_cm=3600, center_y_cm=BAY_Y_CENTER, length_cm=(BAY_Y_BACK - BAY_Y_FRONT), along_x=False,
)

unreal.EditorLevelLibrary.save_current_level()

print("Phase 3 greybox: 3 store bays placed (Technology, Fashion, Cafe) with open storefronts onto the corridor, and level saved.")
print("Known follow-up (not done by this script): storefront-facing walls/glass/doors, ceiling, and deciding which mall_units row maps to which bay.")
