import random
from characters import Toby_Sprinkledust, Asterion


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
            attack = random.randint(0, 20)
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
                    print("==========================================")
                    print(f"{player.name} accidentally stabbed the air!")
                    print("==========================================")
            elif selection == "2":
                print(f"{player.name} has rolled a {attack}")
                if attack >= 9:
                    player.sly_flurish(target)
                    if target.health > 0:
                        target.counter_attack(player)
                else:
                    print("==========================================")
                    print(f"{player.name} couldn't sneak up on {target.name}")
                    print("==========================================")
            elif selection == "3":
                player.healing_potion()
                if target.health > 0:
                        target.counter_attack(player)
                        target.counter_attack(player)              
    else:
        return

