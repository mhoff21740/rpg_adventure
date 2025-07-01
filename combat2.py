"""### This will be the new combat system """

import random
from characters import Toby, Asterion, Minsc, Karlach, Laezel, Shadowheart
from constants_and_utlility_funcs import border
from classes import *


def combat_encounter2(player, target):
        while target.health > 0 and player.health > 0:
            selection = input(
                "You need to defend yourself, which action will you take?\n"
                f"{player.attack1_descrip}\n"
                f"{player.attack2_descrip}\n"
                f"{player.heal1_descrip}\n").strip()
            if selection not in ("1", "2", "3"):
                print("You do not know these spells.")
                continue
            attack = random.randint(1, 20)
            if selection == "1":
                print(f"{player.name} has rolled a {attack}")
                if attack >= 9:
                    player.attack1(target)
                    if target.health > 0:
                        target.counter(player)
                else:
                    if isinstance(player, Ranger):
                        if player.arrows > 0:
                            player.arrows -= 1
                            print(border)
                            player.attack1_fail
                            print(border)
                            continue
                        else:
                            print(border)
                            print(f"{player.name} has no arrows and resorts to melee!")
                            player.basic_melee(target)
                            print(border)
                            continue
                    else:
                        print(border)
                        print(f"{player.name}'s attack missed!")  
                        print(border)
                        continue

            elif selection == "2":
                print(f"{player.name} has rolled a {attack}")
                if attack >= 9:
                    player.attack2(target)
                    if target.health > 0:
                        target.counter_attack(player)
                else:
                    print("====================================================================")
                    print(f"{player.name} {player.attack2_fail}!")
                    print("====================================================================")
            elif selection == "3":
                player.heal1()
                if target.health > 0:
                   target.counter(player)
            else:
                return

