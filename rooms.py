from classes2 import Room
from characters import pyrothrax_boss,zelroth_boss,atlas_boss,nakamara_boss,aetherion_boss

# 1. Treasure Vault
treasure_vault = Room(
    description="You step into a glittering chamber where the air shimmers with reflected torchlight, and piles of gold coins and ornate chests beckon.",
    exits={},
    characters=[],
    visited=False,
    secret={}, #"You find an add panel on the ground"
    items=["Gold Coin", "Jeweled Chalice", "Stack of Gems"]
)

# 2. Gem Chamber
gem_chamber = Room(
    description="As you enter, the walls burst into soft light, encrusted with rubies, emeralds, sapphires, and diamond fragments that glow in the torchlight.",
    exits={},
    characters=[],
    visited=False,
    secret={}, #"You search the alter throughly and see an odd button"
    items=["Ruby", "Emerald", "Sapphire", "Diamond Fragment"]
)

# 3. Potion Laboratory
potion_lab = Room(
    description="You push open the door to a laboratory where shelves of shimmering vials line the walls, each liquid swirling with arcane power.",
    exits={},
    characters=[],
    visited=False,
    secret={}, #"There is an empty file that doesnt seem to belong"
    items=["Healing Potion", "Invisibility Draught", "Elixir of Strength"]
)

# 4. Ancient Armory
ancient_armory = Room(
    description="You find yourself in an armory of legend, where enchanted swords and spellproof shields stand ready beneath ornate banners.",
    exits={},
    characters=[],
    visited=False,
    secret={}, #"You see an odd wear pattern on the status gauntletS
    items=["Enchanted Sword", "Spellproof Shield", "Helmet of Insight"]
)

# 5. Elusive Garden
elusive_garden = Room(
    description="You step barefoot into a moonlit garden, exotic flowers perfuming the air and a silent fountain at its center stirring in shadows.",
    exits={},
    characters=[],
    visited=False,
    secret={}, #"There are strange runes on the basin that look like they can be aligned.
    items=["Flower of Renewal", "Bottle of Pure Water"]
)

# 6. Ancient Library
ancient_library = Room(
    description="You push aside a dusty curtain and enter a library of ages, towering bookshelves converging on an open grimoire that hums with ancient knowledge.",
    exits={},
    characters=[],
    visited=False,
    secret={}, #"You see many dusty tomes on this shelf, although one appears to be somewhat cleaner than the rest
    items=["Tome of Knowledge", "Scroll of Fireball"]
)

# Collect all secret rooms
secret_rooms = [
    treasure_vault,
    gem_chamber,
    potion_lab,
    ancient_armory,
    elusive_garden,
    ancient_library
]

secret_room_mapping = {
    "hidden panel": treasure_vault,
    "moss altar": gem_chamber,
    "false shelf": potion_lab,
    "statue gauntlet": ancient_armory,
    "fountain basin": elusive_garden,
    "rotating shelf": ancient_library
}




# Bawss Rooms ( Need to create bosses) # Also maybe make attacks immune until something is done to boss or playterhas something in inv!


# 1. Dragon's Lair
dragon_lair = Room(
    description="""
You step into a vast, molten cavern where rivers of lava carve glowing paths across the black stone floor. The heat is stifling, and each breath tastes of brimstone. At the far end, glowing embers swirl around the massive form of Pyrothrax the Flame Drake.
""",
    exits={},
    characters={"Pyrothrax the Flame Drake": pyrothrax_boss}, 
    visited=False,
    secret={},
    items=["Drakefire Scale", "Flameheart Ruby"]
)


# 2. Ancient Lich's Sanctum
lich_sanctum = Room(
    description="""
The corridor opens into a vaulted chamber lined with obsidian pillars carved in the likeness of wailing souls. In the center sits Zelroth the Eternal upon a throne of bone, his hollow eyes glowing with unholy power.
""",
    exits={},
    characters={"Zelroth the Eternal": zelroth_boss},  
    visited=False,
    secret={},
    items=["Phylactery Shard", "Staff of the Damned"]
)

# 3. Golem Foundry
golem_foundry = Room(
    description="""
Sparks fly and metal groans under the weight of forging arms as you enter the industrial heart of the foundry. Slinging molten steel, the colossal form of Atlas, the Iron Colossus, awakens to your presence.
""",
    exits={},
    characters={"Atlas, the Iron Colossus": atlas_boss},
    visited=False,
    secret={},
    items=["Colossus Core", "Golem Gauntlet"]
)

# 4. Serpent Queen's Temple
serpent_temple = Room(
    description="""
Vines creep down moss-covered walls and the air is thick with venomous mist. Golden serpent statues surround a raised dais where Nakamara the Serpent Queen coils, her forked tongue tasting the air in anticipation.
""",
    exits={},
    characters={"Nakamara the Serpent Queen": nakamara_boss},
    visited=False,
    secret={},
    items=["Queen's Fang", "Venomous Scepter"]
)

# 5. Sky Fortress Throne
sky_throne = Room(
    description='''
You descend a spiraling stone stair into a sprawling vaulted hall hewn from storm-battered granite. Flickering torch sconces line the damp walls, their smoke curling toward arched ceilings carved with tempest motifs. Gusts howl through grated vents overhead, stirring puddles on the flagstone floor. Atop a jagged dais of black basalt stands Lord Aetherion, Stormwarden of the Deep Holds—his rune-inscribed armor crackling with raw lightning.
''',
    exits={},
    characters={ "Lord Aetherion, Stormwarden of the Deep Holds": aetherion_boss},
    visited=False,
    secret={},
    items=["Stormwarden’s Pauldrons", "Gale-forged Blade"]
)


# Collection for easy iteration
boss_rooms = [dragon_lair, lich_sanctum, golem_foundry, serpent_temple, sky_throne]



















###################################################### Room Descriptions for main campaign, leave here until I figure out where else I can put them    ################################################################








room_descriptions = [
    "You enter a grand hall lined with faded banners and cracked marble pillars.",
    "You step into a chamber filled with the scent of old parchment and shelves of dusty tomes.",
    "You walk into a circular room illuminated by a flickering blue light and a mosaic floor.",
    "You find yourself in a damp cellar, water dripping steadily from the ceiling.",
    "You step over broken armor and shattered shields that litter the floor of this abandoned armory.",
    "You ascend a spiral staircase winding up the center of this narrow, torch-lit tower.",
    "You are surrounded by walls covered in strange, glowing runes that pulse softly.",
    "You step into a greenhouse overrun with tangled vines and exotic plants.",
    "You enter a room that is eerily silent, with a single, ancient statue standing in the center.",
    "You feel a cold draft as you walk through a corridor lined with barred prison cells.",
    "You arrive in a kitchen, pots and pans scattered as if someone left in a hurry.",
    "You step into a crypt where a low mist clings to the floor and stone coffins line the walls.",
    "You enter a chamber filled with gears and levers, the remnants of a forgotten machine.",
    "You walk into a lavish bedroom, the bed draped in velvet and a cracked mirror on the wall.",
    "You find yourself in a circular chamber with a domed ceiling, painted with faded constellations.",
    "You step into a library with toppled shelves and torn scrolls scattered across the floor.",
    "You descend into a musty wine cellar, broken bottles and the scent of old grapes filling the air.",
    "You wade into a sunken chamber, ankle-deep in murky water and crawling with frogs.",
    "You enter a gallery of faded portraits, their eyes seeming to follow your every move.",
    "You step into a forge, cold and abandoned, with rusted tools and a pile of coal.",
    "You walk down a narrow hallway, its walls scratched with desperate messages.",
    "You enter a room filled with shattered mirrors, reflecting your image in a thousand shards.",
    "You step into a dusty trophy room, animal heads and strange artifacts lining the walls.",
    "You arrive in a chapel with broken pews and a shattered stained glass window.",
    "You enter a laboratory cluttered with bubbling potions and mysterious devices.",
    "You step onto a balcony overlooking a misty abyss, the railing dangerously loose.",
    "You find yourself in a child's nursery, toys scattered and a rocking horse gently swaying.",
    "You enter a pantry, shelves bare except for a single, moldy loaf of bread.",
    "You walk into a music room, a grand piano covered in dust and a harp with broken strings.",
    "You step into a prison guardroom, overturned chairs and a ring of keys on the floor.",
    "You enter a map room, walls covered in faded charts and a compass spinning wildly.",
    "You discover a secret armory, racks of weapons hidden behind a false wall.",
    "You wade through a flooded passage, water lapping at the stone steps.",
    "You enter a room filled with cobwebs, spiders scurrying as you arrive.",
    "You step into a grand ballroom, its floor cracked and a chandelier hanging by a thread."
]



all_items = [
    "map", "lantern", "torch", "sword", "shield", "goldcoin", "bread", "turtle", "toilet", "sweet_roll", "cheesewheel", "old boot", "fishing rod", "chair", "goldfish", "magic wand", "rusty key", "healing potion", "silver dagger", "ancient coin", "magic scroll", "rope", "emerald ring", "leather boots", "iron helmet", "mysterious amulet", "crystal orb", "broken shield", "lockpick set", "vial of poison", "map fragment", "enchanted cloak", "dragon scale", "goblet of wine", "ancient tome", "bag of gems", "silver flute", "potion of invisibility", "cursed ring", "elven arrow", "wizard's hat", "arrow",
    "grappling hook", "oil flask", "tinderbox", "waterskin", "crowbar", "shovel", "hammer", "nails", "chalk", "mirror", "bell", "whistle", "spool of thread", "needle", "empty vial", "bucket", "blanket", "piton", "spyglass", "signal whistle"
]