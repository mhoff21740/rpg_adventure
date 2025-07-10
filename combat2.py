"""### This will be the new combat system """

from enum import Enum
import random
from characters import Toby, Asterion, Minsc, Karlach, Laezel, Shadowheart
from constants_and_utlility_funcs import border
from classes2 import *



def combat_encounter3(player, target):
    if player.level >= target.level:
        target.enemy_scailing(player)
    while target.health > 0 and player.health > 0:
        # List built from classes attributes to allow for easy indexing and calling
        actions = [
            {"func": player.attack1, "desc": player.attack1_descrip, "fail": player.attack1_fail},
            {"func": player.attack2, "desc": player.attack2_descrip, "fail": player.attack2_fail},
            {"func": player.heal1,    "desc": player.heal1_descrip,    "heal": True}
        ]
        if player.level >= 2:
            actions += [
                {"func": player.attack3, "desc": player.attack3_descrip, "fail": player.attack3_fail},
                {"func": player.attack4, "desc": player.attack4_descrip, "fail": player.attack4_fail},
            ]
        if player.level >= 3:
            actions += [
                {"func": player.attack5, "desc": player.attack5_descrip, "fail": player.attack5_fail},
                {"func": player.attack6, "desc": player.attack6_descrip, "fail": player.attack6_fail},
            ]
        if player.level >= 4:
            actions += [
                {"func": player.attack7, "desc": player.attack7_descrip, "fail": player.attack7_fail},
                {"func": player.attack8, "desc": player.attack8_descrip, "fail": player.attack8_fail},
            ]
        if player.level >= 5:
            actions += [
                {"func": player.attack9,  "desc": player.attack9_descrip,  "fail": player.attack9_fail},
                {"func": player.attack10, "desc": player.attack10_descrip, "fail": player.attack10_fail},
            ]

        # combat begin
        prompt = "\nYou need to defend yourself, which action will you take?\n"
        for i, action in enumerate(actions):
            prompt += f"{action['desc']}\n"
        selection = input(prompt).strip()
        if not selection.isdigit() or not (1 <= int(selection) <= len(actions)):
            print("You do not know these spells.")
            continue
        selected_action = int(selection) - 1 #<--This converts player selection back to index counting logic, so we can grab the correct attack( ie. firebolt, iceshard, etc)  (Since its starts at the 0 index position). 
        attack = actions[selected_action] #<- index position of  of desired attack( I.e I want to use Ice Shard this round, the description says 2, but its really at index 1)
        if attack.get("heal"):
            player.heal1()
            if target.health > 0:
                target.counter(player)
            continue
        attack_roll = random.randint(1, 20)
        print(f"{player.name} has rolled a {attack_roll}\n")
        if attack_roll >= 9:
            # Successful hit
            attack["func"](target) #<--calls the method from the players desired attack
            if target.health > 0:
                target.counter(player)
        else:
            if attack["func"] == player.attack1 and hasattr(player, "arrows"):
                if player.arrows > 0:
                    print(border)
                    attack["fail"]()
                    print(border)
                    continue
                else:
                    print(border)
                    print(f"{player.name} has no arrows and resorts to melee!")
                    player.basic_melee(target)
                    print(border)
                    continue
            print(border)
            fail = attack.get("fail")
            if callable(fail):
                print(fail() or "")
            elif isinstance(fail, str):
                print(f" {player.name} {fail} {target.name}.")
            else:
                print(f"{player.name}'s attack missed!")
            print(border)


