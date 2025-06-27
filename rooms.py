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
    characters= None,
    visited=False,
    items=["goldcoin", "bread", "turtle","toilet"]
)

east_room = Room(
    description="You are in a narrow corridor lit by flickering torches. The floor is covered in dust and old footprints.",
    exits={},  # placeholder
    characters=None,
    visited=False,
    items=["sweet_roll", "cheesewheel", "old boot","fishing rod"],
)

west_room = Room(
    description="You are in a cramped chamber filled with cobwebs. Broken furniture lies scattered across the floor.",
    exits={},  # placeholder
    characters=None,
    visited=False,
    items=["chair", "goldfish", "magic wand"]
)

# Now set the actual exits using room references

center_room.exits = {"east":east_room}

rooms_list = [north_room, south_room, east_room, west_room]

all_exits = {"north":north_room, "south":south_room, "east":east_room, "west":west_room, "center":center_room}

room_descriptions = [
    "You enter a grand hall lined with faded banners and cracked marble pillars.",
    "This chamber is filled with the scent of old parchment and shelves of dusty tomes.",
    "A flickering blue light illuminates a circular room with a mosaic floor.",
    "You find yourself in a damp cellar, water dripping steadily from the ceiling.",
    "Broken armor and shattered shields litter the floor of this abandoned armory.",
    "A spiral staircase winds up the center of this narrow, torch-lit tower.",
    "The walls here are covered in strange, glowing runes that pulse softly.",
    "You step into a greenhouse overrun with tangled vines and exotic plants.",
    "This room is eerily silent, with a single, ancient statue standing in the center.",
    "A cold draft blows through a corridor lined with barred prison cells.",
    "You are in a kitchen, pots and pans scattered as if someone left in a hurry.",
    "A low mist clings to the floor of this crypt, where stone coffins line the walls.",
    "This chamber is filled with gears and levers, the remnants of a forgotten machine.",
    "You enter a lavish bedroom, the bed draped in velvet and a cracked mirror on the wall.",
    "A circular chamber with a domed ceiling, painted with faded constellations."
]



all_items = [
    "map",
    "lantern",
    "torch",
    "sword",
    "shield",
    "goldcoin",
    "bread",
    "turtle",
    "toilet",
    "sweet_roll",
    "cheesewheel",
    "old boot",
    "fishing rod",
    "chair",
    "goldfish",
    "magic wand",
    "rusty key",
    "healing potion",
    "silver dagger",
    "ancient coin",
    "magic scroll",
    "rope",
    "emerald ring",
    "leather boots",
    "iron helmet",
    "mysterious amulet",
    "crystal orb",
    "broken shield",
    "lockpick set",
    "vial of poison",
    "map fragment",
    "enchanted cloak",
    "dragon scale",
    "goblet of wine",
    "ancient tome",
    "bag of gems",
    "silver flute",
    "potion of invisibility",
    "cursed ring",
    "elven arrow",
    "wizard's hat",
    "arrow"
]