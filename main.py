from characters import *
from combat import *
from rooms import *
from exploration import *
from constants_and_utlility_funcs import *
from classes import *



def main():
    print("Welcome adventurer!\nPlease select a character!")
    while True:
        character = input("Would you like to play as: Toby, Minsc, or Asterion?\n")
        if character == "Toby":
            print("You have selected the Gnomish Wizard, Toby Sprinkledust!")
            input("Press Enter to Begin!")
            selected_character = Toby_Sprinkledust
            break
        elif character == "Asterion":
            print("You have selected the vamperic rogue Asterion!")
            input("Press enter to continue")
            selected_character = Asterion
            break
        elif character == "Minsc":
            print("You have selected the human ranger, Minsc!")
            input("Press enter to begin")
            selected_character = Minsc
            break
        else:
            print("That character is not playable.")

    # Dungeon setup 
    Room.randomize_character_spawn(rooms_list, character_list, selected_character)
    for room in rooms_list:
        room.randomize_items_in_rooms(all_items, 5)
        room.randomize_room_descriptions(room_descriptions)
        room.randomize_room_exits(all_exits)
    exploration(selected_character)
    
    
main()



'''#########################################################################################################

*Create MASTER DUNGEON GENERATOR, that will generate a truley random senerio each time(random rooms numbers, items, character encounters, exits, etc)!
    *Once that is done, work on expanding dung rooms etc
*Update readme.
* Do something with inv? Maybe have ability to drop item into a room and add it to the rooms current item stash
*Flesh out dnd inheritence classes
*Enhance combats, with mana, and stam , maybe turn combat into a grid based system. Player initalizes combat, then players enter a positonal
grid to do area attacks?
* When I am feeling brave: Implement a system of movement within rooms? Dunno what that would look like, but here we are! 
*Create random add enemies that can be slain easily, and may drop items which will then populate room. 
* Have other NPC's drop items?
* Add leveling system 
################################################################################################################# '''
