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
    
    
if __name__ == "__main__":
    main()

