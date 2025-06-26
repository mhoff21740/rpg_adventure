
from characters import *
from combat import *
from rooms import *
from exploration import *
from constants_and_utlility_funcs import *
from classes import *



def main():
    print ("Welcome adventurer!\nPlease select a character!")
    while True:
        character = input("Would you like to play as: Toby or Asterion?\n")
        if character == "Toby":
            print("You have selected the Gnomish Wizard, Toby Sprinkledust!")
            input("Press Enter to Begin!")
            print (boarder)
            randomize_character_spawn(rooms_list, Asterion)
            randomize_items_in_rooms(all_items,rooms_list)
            exploration(Toby_Sprinkledust)
            break
        if character == "Asterion":
            print("You have selected the vamperic rogue Asterion!")
            input("Press enter to continue")
            randomize_character_spawn(rooms_list, Toby_Sprinkledust)
            randomize_items_in_rooms(all_items,rooms_list)
            exploration(Asterion)
            break
        else:
            print("That character is not playable")
            
    
    
            
    
main()
    
    
'''#########################################################################################################
* Do something with inv? Maybe have ability to drop item into a room and add it to the rooms current item stash
*Create moar classes and enemies? Maybe some inheritance stuffs
*Randomize items in each room from a pool of possible items!
*Create a loot item method for room to tidy up explore logic*
################################################################################################################# '''