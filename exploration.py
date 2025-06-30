from rooms import * 
from classes import *
from characters import *
from combat import *
from constants_and_utlility_funcs import *



def exploration(character, starting_room):
    current_room = starting_room
    while character.health > 0:
        if current_room.visited:
            print("You feel like you have been here before\n")
        print(f"{current_room.description}\n")
        if current_room.items == []:
            print( "This room has been thoughly looted\n")
        else:
            print(f"You see some items strewn throughout: {', '.join(current_room.items)}\n")
        if not current_room.characters:
            if current_room.visited:
                print("You see the remains of your previous fights in here, it's quite smelly!\n")
            else:
                print("You see no enemies....yet.\n")
        else:
            print(f"You see some enemies:{', '.join(current_room.characters)}!\n")
        
        print(f"As you look around, you spot a few exits: {', '.join(current_room.exits)}\n")
        current_room.visited = True
        # Main action selection loop
        while True:
            options = [
                "1.) Go through an exit?",
                "2.) Loot some items?\n"
                "3.) Check inventory"
            ]
            if current_room.characters:
                options.append("4.) Engage in combat?")
            selection = input(
                "What would you like to do?\n\n" + "\n".join(options) + "\n"
            )

            valid_choices = ["1", "2", "3"]
            if current_room.characters:
                valid_choices.append("4")

            if selection not in valid_choices:
                print("Those features haven't been implemented yet")
                continue

            if selection == "1":
                # Exit selection loop
                while True:
                    exit_choice = input(
                        f"\nWhich exit would you like to go through: {', '.join(current_room.exits)}?" +"\n"
                    )
                    if exit_choice not in current_room.exits:

                        print("You cannot exit through a wall")
                        continue
                    else:
                        current_room = current_room.exits[exit_choice]
                        print(f"\n{border}\n\n\n")
                        break  # Exit the exit selection loop
                break  # Exit the main action selection loop to refresh room

            elif selection == "2":
                # Item loot loop
                if not current_room.items:
                    print ("This throughly looted, there is nothing more aside from cobwebs and dust\n")
                else:
                    while True:
                        item_looted = input(
                            f"Which item would you like to loot: {', '.join(current_room.items)}?" +"\n"
                        )
                        if item_looted not in current_room.items:
                            print("That item isn't here")
                            continue
                        elif item_looted in ("toilet", "turtle", "old boot", "chair", "goldfish"):
                            if item_looted == "toilet":
                                print("What are you planning to do with a toilet?!\n"
                                      "You don't know yet, but hey, a toilet is a toilet!\n")
                                current_room.loot_item(character,item_looted)
                                break
                            elif item_looted == "turtle":
                                print('"I think the turtle wants to be left alone."')
                                print("You agree with your conscience and leave him at it.")
                                break
                            elif item_looted == "old boot":
                                print("Maybe I can find the matching one!\n")
                                break
                                current_room.loot_item(character,item_looted)
                            elif item_looted == "chair":
                                print("You can't fit this into your bag\n")
                                break
                            elif item_looted == "goldfish":
                                if "fishing rod" in character.inventory:
                                    current_room.loot_item(character,item_looted)
                                    break
                                else:
                                    print("The goldfish slips through your fingers and swims away. You are still wondering how it got here and managed to survive.\n")
                                    break
                        else:
                            current_room.loot_item(character,item_looted)
                            if not current_room.items:
                                print("This room has been thoroughly looted.\n")
                                break  # Exit the loot loop if no items remain
                            break  # Exit the loot loop after a successful loot
                    # After looting, stay in the same room and allow further actions
            elif selection =="3":
                while True:
                    if character.inventory =={}:
                        print("You have no items in your bag\n")
                        break
                    print (f"You currently have: {', '.join(character.inventory.keys())}")
                    selection = input('Would you like to know the quantity of each item? Please enter "y" or "n": \n')
                    if selection == "y":
                        for item in character.inventory:
                            print(f"{item}:{character.inventory[item]}\n")
                        break
                    else:
                        break
                
            elif selection == "4" and current_room.characters:
                combantant = input(f"Who would you like to fight? {', '.join(current_room.characters)}\n")
                if combantant not in ', '.join( current_room.characters):
                    print(" This enemey is not here\n")
                    continue
                else:
                    combantant = current_room.characters[combantant]
                combat_encounter(character, combantant)
                if character.health <= 0:
                    print("You have been defeated! Game Over!")
                    return
                # Remove the defeated enemy from the room
                if combantant.health <= 0:
                    drop_chance = random.randint(1,2)
                    print(f"You have defeated {combantant.name}!\n")
                    if combantant in character_list:
                        character.gain_xp(int(round(combantant.level * 35)))    
                    else:
                        character.gain_xp(combantant.xp)
                    print (f"\nYou are wounded from that fight and left with only {character.health} HP! You will need to heal at some point!\n")
                    if drop_chance == 1:
                        print(f"As you marval over your victory, you see that {combantant.name} has dropped {", ".join(current_room.random_npc_drops())}\n")
                    del current_room.characters[combantant.name]
                    
                


