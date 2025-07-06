from rooms import * 
from classes2 import *
from characters import *
from combat2 import *
from constants_and_utlility_funcs import *
import time




def exploration(character, starting_room):
    current_room = starting_room
        
    while character.health > 0:
        if current_room.visited:
            print("\033[1mYou feel like you have been here before\033[0m\n")
            time.sleep(1.5)
        print(f"{current_room.description}\n")
        if current_room.items == []:
            print( "This room has been thoughly looted\n")
            time.sleep(1.5)
        else:
            print(f"You see some items strewn throughout: {', '.join(current_room.items)}\n")
            time.sleep(1.5)
        if not current_room.characters:
            if current_room.visited:
                print("You see the remains of your previous fights in here, it's quite smelly!\n")
                time.sleep(1.5)
            else:
                print("You see no enemies....yet.\n")
                time.sleep(1.5)
        else:
            print(f"You see some enemies:{', '.join(current_room.characters)}!\n")
            time.sleep(1.5)
        
        print(f"As you look around, you spot a few exits: {', '.join(current_room.exits)}\n")
        time.sleep(1.5)
        
        # Main action selection loop
        while True:
            options = [
                "1.) Go through an exit?",
                "2.) Loot some items?\n"
                "3.) Check inventory\n"
                "4.) Investigate the room"
            ]
            if current_room.characters:
                options.append("5.) Engage in combat?")
            selection = input(
                "What would you like to do?\n\n" + "\n".join(options) + "\n"
            )

            valid_choices = ["1", "2", "3","4"]
            if current_room.characters:
                valid_choices.append("5")

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
                        current_room.visited = True
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
            
            
            elif selection =="4":
                perception_check = random.randint(1, 20)
                print(f"{character.name} has rolled a perception check of {perception_check}.\n")
                if current_room.secret:
                    if perception_check >= 12:
                        for secret_item, secret_room in current_room.secret.items():
                            print(f"After an intense investigation, you discover a peculiar {secret}\n")
                            interaction = input("Would you like to interact with it? Y or N\n")
                            if interaction.lower() == "y":
                                # Revels le secret exit and adds to exits in room
                                current_room.exits[f"{secret_item}"] = secret_room
                                secret_room.exits[f"back out"] = current_room
                                print(f"You have revealed a secret passage: secret_{secret}!")
                                current_room = secret_room
                                break
                            elif interaction.lower() == "n":
                                break
                            else:
                                print("Not a valid option")
                else:
                    print("Nothing stands out at you\n")
                    
                
                
            elif selection == "5" and current_room.characters:
                combantant = input(f"Who would you like to fight? {', '.join(current_room.characters)}\n")
                if combantant not in ', '.join( current_room.characters):
                    print(" This enemey is not here\n")
                    continue
                else:
                    combantant = current_room.characters[combantant]
                combat_encounter3(character, combantant)
                if character.health <= 0:
                    print("You have been defeated! Game Over!")
                    return
                # Remove the defeated enemy from the room
                if combantant.health <= 0:
                    print(f"You have defeated {combantant.name}!\n")
                    if combantant in character_list:
                        character.gain_xp(int(round(combantant.level * 35)))    
                    else:
                        character.gain_xp(combantant.xp)
                    if isinstance(character, Wizard):
                        character.spell_slotz()
                    drop_chance = random.randint(1,2)
                    print (f"\nYou are wounded from that fight and left with only {character.health} HP! You will need to heal at some point!\n")
                    if drop_chance == 1:
                        print(f"As you marval over your victory, you see that {combantant.name} has dropped {", ".join(current_room.random_npc_drops())}\n")
                    del current_room.characters[combantant.name]
                    
                


