"""
Phase 3 Greybox — place a PlayerStart at the mall entrance.

Run AFTER phase3_greybox_floors.py, phase3_greybox_walls.py, and
phase3_greybox_bays.py. Requires: Python Editor Script Plugin enabled.
Run via: Tools > Execute Python Script... > select this file > Open.

What this does:
  - Spawns one PlayerStart actor just inside the atrium's south entrance
    gap (see MALL_LAYOUT.md: 4m gap centered at X=0, wall line Y=-1200),
    facing north (+Y) into the atrium.
  - Removes any PlayerStart actor this script previously placed (by
    label), so it's safe to re-run without leaving duplicates.

What this does NOT do:
  - Does not add a Character/Pawn to walk with — that's a separate,
    manual step (see below) because it uses Epic's official "First
    Person" content pack rather than a hand-built Blueprint, which is
    more reliable than generating Blueprint logic through a script that
    can't be tested here.
  - Does not change Project Settings (Default Pawn Class) — manual step,
    see below.

How to get an actual walking (not flying) first-person character, after
running this script:
  1. Content Browser -> the green "Add" button -> "Add Feature or Content
     Pack..." -> "Blueprint Feature Packs" tab -> "First Person" -> Add to
     Project. This adds Epic's own tested First Person Character
     Blueprint plus its Enhanced Input assets under Content/FirstPerson/.
  2. Edit > Project Settings > search "Default Pawn Class" (under
     Engine > Maps & Modes > Selected GameMode) -> set it to the new
     first-person Character Blueprint that pack just added.
  3. Press Play. You should now walk (with gravity/collision) instead of
     flying, spawning at the PlayerStart this script placed.
"""

import unreal

editor_actor_subsystem = unreal.get_editor_subsystem(unreal.EditorActorSubsystem)

PLAYER_START_LABEL = "PlayerStart_MallEntrance_Greybox"


def destroy_actor_by_label(label):
    for actor in editor_actor_subsystem.get_all_level_actors():
        if actor.get_actor_label() == label:
            editor_actor_subsystem.destroy_actor(actor)
            return True
    return False


removed = destroy_actor_by_label(PLAYER_START_LABEL)
if removed:
    print("Removed previously placed {} before re-placing it.".format(PLAYER_START_LABEL))

# Just inside the atrium's south entrance gap (X -200..200 at Y=-1200 is
# the wall line itself), facing north (+Y) into the atrium.
location = unreal.Vector(0.0, -1000.0, 100.0)
rotation = unreal.Rotator(0.0, 90.0, 0.0)  # (Roll, Pitch, Yaw) - Yaw=90 faces +Y

actor = editor_actor_subsystem.spawn_actor_from_class(unreal.PlayerStart, location, rotation)
actor.set_actor_label(PLAYER_START_LABEL)

unreal.EditorLevelLibrary.save_current_level()

print("Phase 3 greybox: PlayerStart placed at the mall entrance, facing into the atrium, and level saved.")
print("Next (manual, not scriptable reliably): add Epic's First Person content pack and set it as the Default Pawn Class - see this script's docstring for the exact steps.")
