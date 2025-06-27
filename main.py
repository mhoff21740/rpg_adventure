
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
            print("That character is not playable.")
            
    
    
            
    
main()
    
    
'''#########################################################################################################
*Update readme.
* Do something with inv? Maybe have ability to drop item into a room and add it to the rooms current item stash
*Flesh out dnd inheritence classes
*Enhance combats, with mana, and stam , maybe turn combat into a grid based system. Player initalizes combat, then players enter a positonal
grid to do area attacks?
* When I am feeling brave: Implement a system of movement within rooms? Dunno what that would look like, but here we are! 
################################################################################################################# '''