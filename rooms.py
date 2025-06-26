from characters import *
from classes import Room

center_room = Room(
    description="You are in the center of a mysterious labyrinth. Faint light filters in from cracks above, and passages lead in all directions.",
    exits={},  # will be set later
    characters=None,
    visited=False,
    items=["map", "lantern"]
)

north_room = Room(
    description="You are in a dark, cold room with stone walls. The air is damp and musty.",
    exits={},  # placeholder
    characters=None,
    visited=False,
    items=["torch", "sword", "shield"]
)

south_room = Room(
    description="You are in an eerie warm room with moss covered wall. The air is damp and stanky",
    exits={},  # placeholder
    characters=Asterion,
    visited=False,
    items=["goldcoin", "bread", "turtle","toilet"]
)

east_room = Room(
    description="You are in a narrow corridor lit by flickering torches. The floor is covered in dust and old footprints.",
    exits={},  # placeholder
    characters=None,
    visited=False,
    items=["sweet_roll", "cheesewheel", "old_boot"],
)

west_room = Room(
    description="You are in a cramped chamber filled with cobwebs. Broken furniture lies scattered across the floor.",
    exits={},  # placeholder
    characters=None,
    visited=False,
    items=["chair", "goldfish", "magic_wand"]
)

# Now set the actual exits using room references
north_room.exits = {"south": south_room, "east": east_room, "center":center_room}
south_room.exits = {"north": north_room}
east_room.exits = {"west": west_room, "center":center_room}
west_room.exits = {"east": east_room, "center":center_room}
center_room.exits = {"north":north_room, "south":south_room, "east":east_room, "west":west_room}