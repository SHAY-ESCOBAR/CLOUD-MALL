"""
Greybox cleanup — remove duplicate actors left over from re-running the
Phase 3 placement scripts (phase3_greybox_floors.py in particular was run
more than once on the same level).

Run via: Tools > Execute Python Script... > select this file > Open.
Safe to re-run; it only ever removes exact-label duplicates and always
keeps exactly one copy of each.

What this does:
  - Scans every actor in the current level.
  - Groups them by their exact label (e.g. "SM_MainCorridorFloor_Greybox").
  - For any label with more than one actor, keeps the first one found and
    destroys the rest.
  - Saves the level afterward.
  - Prints exactly what it removed, so nothing disappears silently.

What this does NOT do:
  - Does not touch actors with unique labels (walls, bays, PlayerStart,
    lights, etc. are untouched if there's only one of each).
  - Does not delete anything outside the current open level.
"""

import unreal
from collections import defaultdict

editor_actor_subsystem = unreal.get_editor_subsystem(unreal.EditorActorSubsystem)

by_label = defaultdict(list)
for actor in editor_actor_subsystem.get_all_level_actors():
    by_label[actor.get_actor_label()].append(actor)

removed_count = 0
for label, actors in by_label.items():
    if len(actors) <= 1:
        continue
    keep, extras = actors[0], actors[1:]
    for extra in extras:
        editor_actor_subsystem.destroy_actor(extra)
        removed_count += 1
    print("Kept 1x '{}', removed {} duplicate(s).".format(label, len(extras)))

if removed_count:
    unreal.EditorLevelLibrary.save_current_level()
    print("Greybox cleanup: removed {} duplicate actor(s) total and saved the level.".format(removed_count))
else:
    print("Greybox cleanup: no duplicates found, nothing changed.")
