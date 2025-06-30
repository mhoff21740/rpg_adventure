from classes import *

# This is the current list of playable characters in the Faerun

# These are all level 1 ##

Toby_Sprinkledust = Wizard("Toby Sprinkledust", 18, 5, 5, 2, 1, 0, 1)
Asterion = Rogue("Asterion", 16, 2, 2, 6, 4, 0, 1)
Minsc = Ranger("Minsc", 17, 2, 2, 6, 5, 10, 0, 1)
Karlach = Barbarian("Karlach", 20, 1, 1, 3, 6, 0, 1)
Laezel  = Fighter("Lae'zel", 18, 2, 2, 5, 5, 0, 1)
Shadowheart = Paladin("Shadowheart", 18, 2, 5, 3, 4, 0, 1)



character_list = [Toby_Sprinkledust, Asterion,Minsc, Karlach, Laezel, Shadowheart]
character_names = [ c.name for c in character_list]

print(Toby_Sprinkledust.create_class_variable())