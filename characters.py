from classes2 import *

# This is the current list of playable characters in the Faerun

# These are all level 1 ##

Toby = Wizard("Toby", 18, 5, 5, 2, 1, 0, 1)
Asterion = Rogue("Asterion", 16, 2, 2, 6, 4, 0, 1)
Minsc = Ranger("Minsc", 17, 2, 2, 6, 5, 3, 0, 1)
Karlach = Barbarian("Karlach", 20, 1, 1, 3, 6, 0, 1)
Laezel  = Fighter("Lae'zel", 18, 2, 2, 5, 5, 0, 1)
Shadowheart = Paladin("Shadowheart", 18, 2, 5, 3, 4, 0, 1)



character_list = [Toby, Asterion,Minsc, Karlach, Laezel, Shadowheart]
character_names = [ c.name for c in character_list]



# Bosses

pyrothrax_boss  = Boss("Pyrothrax the Flame Drake", 115, 5, 4, 3, 6, 100)
zelroth_boss = Boss("Zelroth the Eternal", 95, 6, 6, 3, 3, 90)
atlas_boss = Boss("Atlas, the Iron Colossus", 120, 3, 3, 2, 6, 85)
nakamara_boss = Boss("Nakamara the Serpent Queen", 100, 5, 5, 6, 4, 95)
aetherion_boss = Boss("Lord Aetherion, Stormwarden of the Deep Holds", 110, 6, 4, 5, 5, 100)

boss_list = [pyrothrax_boss, zelroth_boss, atlas_boss, nakamara_boss, aetherion_boss]
