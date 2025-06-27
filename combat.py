import random
from characters import Toby_Sprinkledust, Asterion, Minsc
from constants_and_utlility_funcs import boarder


def combat_encounter(player, target):
    if player == Toby_Sprinkledust:
        while target.health > 0 and player.health > 0:
            selection = input(
                "You need to defend yourself, which action will you take?\n"
                
                "1.) Cast Fireball - deals moderate fire damage.\n"
                
                "2.) Cast Ice Shard - deals light cold damage.\n"
                
                "3.) Cast Healing Word - restores a small amount of health\n"
            ).strip()
            if selection not in ("1", "2", "3"):
                print("You do not know these spells.")
                continue
            attack = random.randint(1, 20)
            if selection == "1":
                print(f"{player.name} has rolled a {attack}")
                if attack >= 9:            
                    player.cast_fireball(target)
                    if target.health > 0:
                        target.counter_attack(player)
                else:
                    print("==================================================================")
                    print(f"{player.name} accidentally launched a fireball over {target.name}")
                    print("==================================================================")
            elif selection == "2":
                print(f"{player.name} has rolled a {attack}")
                if attack >= 9:
                    player.cast_ice_shard(target)
                    if target.health > 0:
                        target.counter_attack(player)
                else:
                    print("====================================================================")
                    print(f"{player.name} accidentally launched an ice shard over {target.name}")
                    print("====================================================================")
            elif selection == "3":
                player.healing_word()
                if target.health > 0:
                   target.counter_attack(player)
                   target.counter_attack(player)
                     
                        
    elif player == Asterion:
        while target.health > 0 and player.health > 0:
            selection = input(
                "You need to defend yourself, which action will you take?\n"
                
                "1.) Stab with your rapier - deals moderate stab damage.\n"
                
                "2.) Sly Flurish - deals light stab damage.\n"
                
                "3.) Drink a healing potion - restores a small amount of health\n"
            ).strip()
            if selection not in ("1", "2", "3"):
                print("You are untrained in those skills.")
                continue
            attack = random.randint(1, 20)
            if selection == "1":
                print(f"{player.name} has rolled a {attack}")
                if attack >= 9:
                    player.rapier_stab(target)
                    if target.health > 0:
                        target.counter_attack(player)
                else:
                    print("============================================")
                    print(f"{player.name} accidentally stabbed the air!")
                    print("============================================")
            elif selection == "2":
                print(f"{player.name} has rolled a {attack}")
                if attack >= 9:
                    player.sly_flurish(target)
                    if target.health > 0:
                        target.counter_attack(player)
                else:
                    print("=================================================")
                    print(f"{player.name} couldn't sneak up on {target.name}")
                    print("=================================================")
            elif selection == "3":
                player.healing_potion()
                if target.health > 0:
                        target.counter_attack(player)
                        target.counter_attack(player)
                                      
    
    elif player == Minsc:
        while player.health > 0 and target.health > 0:
            selection = input(
                "You need to defend yourself, which action will you take?\n"
                
                "1.) Bow Shot - deals moderate peirce damage.\n"
                
                "2.) Basic Melee - deals light slash damage.\n"
                
                "3.) Drink a healing potion - restores a small amount of health\n"
            ).strip()
            if selection not in ["1", "2", "3"]:
                print("You do not have these abilities")
                continue
            attack_roll = random.randint(1, 20)
            if selection == "1":
                print(f"{player.name} has rolled a {attack_roll}")
                if attack_roll > 9:
                    player.bow_shot(target)
                    if target.health > 0:
                        target.counter_attack(player)
                else:
                    if player.arrows > 0:
                        print(boarder)
                        print(f"{player.name}'s vision was impaired and he has launched an arrow over {target.name}")
                        player.arrows -= 1
                        print(f"As a result of that blunder, {player.name} now has {player.arrows} arrows")
                        print (boarder)
                    else:
                        player.basic_melee(target)
           
            elif selection == "2":
                print(f"{player.name} has rolled a {attack_roll}")
                if attack_roll > 9:
                    player.basic_melee(target)
                    if target.health > 0:
                        target.counter_attack(player)
                else:
                    print(boarder)
                    print(f"{player.name} has missed {target.name}")
                    print (boarder) 

            elif selection =="3":
                player.healing_potion()
                if target.health > 0:
                    target.counter_attack(player)
                    target.countrt_attack(player)       

    
    else:
        return

