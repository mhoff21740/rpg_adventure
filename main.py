from characters import *
from combat import *
from rooms import room_descriptions, all_items
import exploration
from constants_and_utlility_funcs import *
from classes import *



def main():
    print("Welcome adventurer!\nPlease select a character!")
    while True:
        character = input(f"Would you like to play as: {', '.join(character_names)}\n")
        if character == "Toby":
            print("You have selected the Gnomish Wizard, Toby Sprinkledust!")
            input("Press Enter to Begin!\n")
            selected_character = Toby
            break
        elif character == "Asterion":
            print("You have selected the vampiric rogue Asterion!")
            input("Press enter to begin!\n")
            selected_character = Asterion
            break
        elif character == "Minsc":
            print("You have selected the human ranger, Minsc!")
            input("Press enter to begin\n")
            selected_character = Minsc
            break
        elif character == "Karlach":
            print("You have selected Karlach, the fierce Tiefling Barbarian!")
            input("Press enter to begin\n")
            selected_character = Karlach
            break
        elif character == "Lae'zel":
            print("You have selected Lae'zel, the relentless Githyanki Fighter!")
            input("Press enter to begin\n")
            selected_character = Laezel
            break
        elif character == "Shadowheart":
            print("You have selected Shadowheart, the mysterious Elf Paladin!")
            input("Press enter to begin\n")
            selected_character = Shadowheart
            break
        else:
            print("That character is not playable.")

    # Dungeon setup
    scenario_room_list = Room.dungeon_room_randomizer(character_list)
    for room in scenario_room_list:
        room.randomize_items_in_rooms(all_items, 5)
        room.randomize_room_descriptions(room_descriptions)
    starting_room = scenario_room_list[0]
    exploration.exploration(selected_character, starting_room)

if __name__ == "__main__":
    main()






"""
Incase I make code impload

def main():
    print("Welcome adventurer!\nPlease select a character!")
    while True:
        character = input(f"Would you like to play as: {', '.join(character_names)}\n")
        if character == "Toby":
            print("You have selected the Gnomish Wizard, Toby Sprinkledust!")
            input("Press Enter to Begin!\n")
            selected_character = Toby
            break
        elif character == "Asterion":
            print("You have selected the vampiric rogue Asterion!")
            input("Press enter to begin!\n")
            selected_character = Asterion
            break
        elif character == "Minsc":
            print("You have selected the human ranger, Minsc!")
            input("Press enter to begin\n")
            selected_character = Minsc
            break
        elif character == "Karlach":
            print("You have selected Karlach, the fierce Tiefling Barbarian!")
            input("Press enter to begin\n")
            selected_character = Karlach
            break
        elif character == "Lae'zel":
            print("You have selected Lae'zel, the relentless Githyanki Fighter!")
            input("Press enter to begin\n")
            selected_character = Laezel
            break
        elif character == "Shadowheart":
            print("You have selected Shadowheart, the mysterious Elf Paladin!")
            input("Press enter to begin\n")
            selected_character = Shadowheart
            break
        else:
            print("That character is not playable.")

    # Dungeon setup
    scenario_room_list = Room.dungeon_room_randomizer()
    Room.randomize_character_spawn(scenario_room_list, character_list, selected_character)

    for room in scenario_room_list:
        room.randomize_items_in_rooms(all_items, 5)
        room.randomize_room_descriptions(room_descriptions)
    starting_room = scenario_room_list[0]
    exploration.exploration(selected_character, starting_room)

if __name__ == "__main__":
    main()

"""