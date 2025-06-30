from classes import *

# This is the current list of playable characters in the Faerun

Toby_Sprinkledust = Wizard("Toby Sprinkledust", 75, 16, 12, 0, 0, 0, 1)
Asterion = Rogue("Asterion", 85, 0, 0, 14, 10, 0, 1 )
Minsc = Ranger("Minsc", 85, 0, 0, 14, 12, 3, 0, 1)
Karlach = Barbarian("Karlach", 85, 0, 0, 10, 18, 0, 1)
Laezel = Fighter("Lae'zel", 85, 0, 0, 12, 15, 0, 1)
Shadowheart = Paladin("Shadowheart", 80, 0, 14, 10, 13, 0, 1)

character_list = [Toby_Sprinkledust, Asterion,Minsc, Karlach, Laezel, Shadowheart]
character_names = [ c.name for c in character_list]