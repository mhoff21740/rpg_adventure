from rooms import * 
from characters import *
from combat import *
from constants_and_utlility_funcs import *

def exploration(character):
    current_room = center_room
    while character.health > 0:
        if current_room.visited:
            print("You feel like you have been here before\n"
                  
            )
        print(f"{current_room.description}\n")
        print(f"You see on a table beside you: {', '.join(current_room.items)}\n")
        if current_room.characters is None:
            print("You see no enemies....yet.\n")
        else:
            print(f"You find another adventurer, {current_room.characters.name}\n")
        
        print(f"As you look around, you spot a few exits: {', '.join(current_room.exits.keys())}\n")
        current_room.visited = True
        # Main action selection loop
        while True:
            options = [
                "1.) Go through an exit?",
                "2.) Loot some items?\n"
                "3.) Check inventory"
            ]
            if current_room.characters is not None:
                options.append("4.) Engage in combat?")
            selection = input(
                "What would you like to do?\n\n" + "\n".join(options) + "\n"
            )

            valid_choices = ["1", "2", "3"]
            if current_room.characters is not None:
                valid_choices.append("4")

            if selection not in valid_choices:
                print("Those features haven't been implemented yet")
                continue

            if selection == "1":
                # Exit selection loop
                while True:
                    exit_choice = input(
                        f"\nWhich exit would you like to go through: {', '.join(current_room.exits.keys())}?" +"\n"
                    )
                    if exit_choice not in current_room.exits:
                        print("You cannot exit through a wall")
                        continue
                    else:
                        current_room = current_room.exits[exit_choice]
                        print(f"\n{boarder}\n\n\n")
                        break  # Exit the exit selection loop
                break  # Exit the main action selection loop to refresh room

            elif selection == "2":
                # Item loot loop
                while True:
                    item_looted = input(
                        f"Which item would you like to loot: {', '.join(current_room.items)}?" +"\n"
                    )
                    if item_looted not in current_room.items:
                        print("That item isn't here")
                        continue
                    elif item_looted in ("toilet", "turtle", "old_boot", "chair", "goldfish"):
                        if item_looted == "toilet":
                            print("What are you planning to do with a toilet?!")
                            current_room.items.remove(item_looted)
                            character.inventory.append(item_looted)
                        elif item_looted == "turtle":
                            print("I think the turtle wants to be left alone")
                            print("You agree with your conscience and leave him at it")
                            break
                        elif item_looted == "old_boot":
                            print("Maybe I can find the matching one!")
                            current_room.items.remove(item_looted)
                            character.inventory.append(item_looted)
                        elif item_looted == "chair":
                            print("You can't fit this into your bag")
                            break
                        elif item_looted == "goldfish":
                            print("The goldfish slips through your fingers and swims away. You are still wondering how it got here and managed to survive.")
                            break
                    else:
                        print(f"You looted the {item_looted}!")
                        current_room.items.remove(item_looted)
                        character.inventory.append(item_looted)
                        
                        break  # Exit the item loot loop
                # After looting, stay in the same room and allow further actions
            elif selection =="3":
                while True:
                    if character.inventory ==[]:
                        print("You have no items in your bag")
                    else:
                        print (f"You currently have: {', '.join(character.inventory)}")
                    break
                
            elif selection == "4" and current_room.characters is not None:
                combat_encounter(character, current_room.characters)
                if character.health <= 0:
                    print("You have been defeated!")
                    return
                # Optionally, remove the defeated enemy from the room
                if current_room.characters.health <= 0:
                    print(f"You have defeated {current_room.characters.name}!\n")
                    current_room.characters = None
                    

