import random
from constants_and_utlility_funcs import border
import functools
import time


## Expanded classes with level up skillz!

# This is a collection of classes that will be used throughoutthe land of Faerun. 

class DND_CLASS:
    def __init__(self, name, health, intelligence, wisdom, dexterity, strength, xp, level, inventory=None):
        self.name = name
        self.health = health
        self.intelligence = intelligence
        self.wisdom = wisdom
        self.dexterity = dexterity
        self.strength = strength
        self.xp = xp
        self.level = level
        self.inventory = {"healing potion": 3 }
        

    def create_class_variable(self): # Used for the bugging of the de. 
        self.vars = {
            key: value
            for key, value in self.__dict__.items()
            if not callable(value)
        }
        return self.vars

    def healing_potion(self):
        heals = round(10 + random.uniform(2, 4))
        self.health += heals
        print(f"{self.name} heals for {heals} -health is now {self.health}")

    
    
    
    def total_level_and_xp(self): #Needed? Maybe if player just wants to remember what their level is 
        print(f"You have {self.xp} xp, you are level {self.level}!")
        return self.xp
    
    def gain_xp(self, xp_dropped):
        self.xp += xp_dropped
        new_level = self.current_level()
        if new_level > self.level:
            self.health += random.randint(4,10)
            print(f"Congratulations! {self.name} has reached level {new_level} and your health has increased to {self.health}!")
            self.level = new_level
            if self.level % 2 != 0 and self.level >= 3:
                while True:
                    print("You have now unlocked an ability point increase!\n")
                    chosen_ability = input("Which ability would you like to increase: intelligence, wisdom, dexterity, or strength?\n")
                    if chosen_ability in ["intelligence", "wisdom", "dexterity", "strength"]:
                        current_value = getattr(self, chosen_ability)
                        setattr(self, chosen_ability, current_value + 2)
                        print(f"{self.name}'s {chosen_ability} is now {getattr(self, chosen_ability)}")
                    else:
                        print("Invalid ability name.")
        else:
            print(f"{self.name} now has gained {xp_dropped} XP and now has a total of {self.xp} XP (Level {self.level})")
    
    def enemy_scailing(self, target):
            self.level = target.level
            for level in range(1, self.level +1):
                self.health += random.randint(4,10)
            
    def current_level(self):
        # Determine level based on XP thresholds
        if self.xp >= 400:
            return 5
        elif self.xp >= 250:
            return 4
        elif self.xp >= 150:
            return 3
        elif self.xp >= 50:
            return 2
        else:
            return 1
        




class Wizard(DND_CLASS):
    def __init__(self, name, health, intelligence, wisdom, dexterity, strength, xp, level=1, spell_slots = 1, inventory=None):
        super().__init__(name, health, intelligence, wisdom, dexterity, strength, xp, level, inventory)
        self.spell_slots = spell_slots
        self.inventory = {"healing potion" : 1 }
        
        # Level-1 spells
        self.attack1 = self.cast_firebolt
        self.attack1_descrip = "1.) Cast Firebolt - moderate fire damage"
        self.attack1_fail = "accidentally launched a fireball over"
        self.attack2 = self.cast_ice_shard
        self.attack2_descrip = "2.) Cast Ice Shard - light cold damage"
        self.attack2_fail = "accidentally launched an ice shard over"
        self.heal1 = self.healing_word
        self.heal1_descrip = "3.) Cast Healing Word - restores a small amount of health"
        self.counter = self.counter_attack

    # Level-2 spells
        self.attack3 = self.cast_scorching_ray
        self.attack3_descrip = "4.) Cast Scorching Ray - two rays of fire"
        self.attack3_fail = "scorching rays sputter harmlessly"
        self.attack4 = self.cast_mirror_image
        self.attack4_descrip = "5.) Cast Mirror Image - create illusory duplicates"
        self.attack4_fail = "images fail to form"

    # Level-3 spells
        self.attack5 = self.cast_lightning_bolt
        self.attack5_descrip = "6.) Cast Lightning Bolt - line of lightning damage"
        self.attack5_fail = "bolt fizzles out"
        self.attack6 = self.cast_invisibility
        self.attack6_descrip = "7.) Cast Invisibility - become unseen"
        self.attack6_fail = "spell fizzles"

    # Level-4 spells
        self.attack7 = self.cast_ice_storm
        self.attack7_descrip = "8.) Cast Ice Storm - area cold damage"
        self.attack7_fail = "storm collapses"
        self.attack8 = self.cast_greater_healing
        self.attack8_descrip = "9.) Cast Greater Healing - restores significant health"
        self.attack8_fail = "healing energy falters"

    # Level-5 spells
        self.attack9 = self.cast_cone_of_cold
        self.attack9_descrip = "10.) Cast Cone of Cold - cone of extreme cold"
        self.attack9_fail = "cone dissipates"
        self.attack10 = self.cast_wall_of_force
        self.attack10_descrip = "11.) Cast Wall of Force - create impassable barrier"
        self.attack10_fail = "barrier fails to materialize"
        
        
    def spell_slotz(self):
        new_level = self.current_level()
        if new_level > self.level:
            self.spell_slots += 2
            print(f"As {self.name} levels up, they have gained {getattr(self,self.spell_slots)} spell slots!")
        else:
            print(f"{self.name} has {self.spell_slots} spell slots remaining.\n")

    # Level-1
    def cast_firebolt(self, target):
        damage = int(round(1 + self.intelligence * 0.5 + self.wisdom * random.uniform(0.3, 0.5)))
        target.health -= damage
        print(border)
        print(f"{self.name} casts Firebolt dealing {damage} damage")
        print(border)
        if target.health <= 0:
            print(f"{target.name} has been made kwispy!\n")
        else:
            print(f"{target.name}'s health is now {target.health}")

    def cast_ice_shard(self, target):
        damage = int(round(1 + self.intelligence * 0.4 + self.wisdom * random.uniform(0.2, 0.3)))
        target.health -= damage
        print(border)
        print(f"{self.name} casts Ice Shard dealing {damage} damage")
        print(border)
        if target.health <= 0:
            print(f"{target.name} has been frozen!\n")
        else:
            print(f"{target.name}'s health is now {target.health}")

    def healing_word(self):
        if self.spell_slots > 0:
            self.spell_slots -= 1
            heals = round(6 + (self.wisdom * random.uniform(1, 4)))
            self.health += heals
            print(f"{self.name} has been healed for {heals}!")
            time.sleep(2)
            print(f"{self.name}'s health is now {self.health}")
        elif self.spell_slots <= 0 and  self.inventory["healing potion"] > 0:
            while True:
                heal_or_not_to_heal = input(f"{self.name} has no more spell slots and cannot heal! You would like to use one of your healing potions? Y or N ")
                if heal_or_not_to_heal.lower() == "y":
                    self.healing_potion()
                    break
                elif heal_or_not_to_heal.lower() == "n":
                    print (f"{self.name} has decided to skip healing")
                    break
                else:
                    print("Invalid selection")
        else:
            print(f"{self.name} has no more spell slots or potions to heal! ")    

    
    
    
    
    def counter_attack(self, target):
        attack = random.choice([self.cast_firebolt, self.cast_ice_shard])
        attack(target)

    # Level-2
    def cast_scorching_ray(self, target):
        rays = 2
        total = 0
        for _ in range(rays):
            bolt_dmg = random.randint(1, 6) + int(self.intelligence * 0.2)
            total += bolt_dmg
        target.health -= total
        print(border)
        print(f"{self.name} casts Scorching Ray, dealing {total} fire damage")
        print(border)
        if target.health <= 0:
            print(f"{target.name} is engulfed in flames!\n")
        else:
            print(f"{target.name}'s health is now {target.health}")

    def cast_mirror_image(self, _=None):
        self.mirror_images = random.randint(2, 4)
        print(f"{self.name} creates {self.mirror_images} illusory duplicates!")

    # Level-3
    def cast_lightning_bolt(self, targets):
        damage = sum(random.randint(1, 6) for _ in range(3)) + int(self.intelligence * 0.2)
        print(border)
        print(f"{self.name} casts Lightning Bolt, dealing {damage} lightning damage!")
        for tgt in targets:
            tgt.health -= damage
            print(f"  – {tgt.name}'s health is now {tgt.health}")
        print(border)

    def cast_invisibility(self, _=None):
        self.invisible = True
        print(f"{self.name} fades from view!")

    # Level-4
    def cast_ice_storm(self, targets):
        damage = sum(random.randint(1, 8) for _ in range(2)) + int(self.wisdom * 0.3)
        print(border)
        print(f"{self.name} casts Ice Storm for {damage} cold damage!")
        for tgt in targets:
            tgt.health -= damage
            print(f"  – {tgt.name}'s health is now {tgt.health}")
        print(border)

    def cast_greater_healing(self):
        heals = round(15 + (self.wisdom * random.uniform(2, 5)))
        self.health += heals
        print(f"{self.name} casts Greater Healing for {heals} health!")
        print(f"{self.name}'s health is now {self.health}")

    # Level-5
    def cast_cone_of_cold(self, targets):
        damage = sum(random.randint(1, 8) for _ in range(3)) + int(self.intelligence * 0.3)
        print(border)
        print(f"{self.name} casts Cone of Cold for {damage} cold damage!")
        for tgt in targets:
            tgt.health -= damage
            print(f"  – {tgt.name}'s health is now {tgt.health}")
        print(border)

    def cast_wall_of_force(self, _=None):
        self.wall_of_force = True
        print(f"{self.name} summons a Wall of Force!")


class Rogue(DND_CLASS):
    def __init__(self, name, health, intelligence, wisdom, dexterity, strength, xp, level=1, inventory=None):
        super().__init__(name, health, intelligence, wisdom, dexterity, strength, xp, level, inventory)
        self.attack1 = self.rapier_stab
        self.attack1_descrip = "1.) Rapier Stab - moderate stab damage"
        self.attack1_fail = "accidentally stabbed the air!"
        self.attack2 = self.sly_flourish
        self.attack2_descrip = "2.) Sly Flourish - light finesse damage"
        self.attack2_fail = "flourish missed its mark!"
        self.heal1 = self.healing_potion
        self.heal1_descrip = "3.) Healing Potion - restores a small amount of health"
        self.counter = self.counter_attack

    # Level-2
        self.attack3 = self.sneak_attack
        self.attack3_descrip = "4.) Sneak Attack - bonus precision damage"
        self.attack3_fail = "failed to find a weak spot"
        self.attack4 = self.cunning_dash
        self.attack4_descrip = "5.) Cunning Dash - reposition quickly"
        self.attack4_fail = "tripped while dashing"
    # Level-3
        self.attack5 = self.evade
        self.attack5_descrip = "6.) Evasion - avoid area attacks"
        self.attack5_fail = "couldn't dodge in time"
        self.attack6 = self.uncanny_dodge
        self.attack6_descrip = "7.) Uncanny Dodge - halve incoming damage"
        self.attack6_fail = "failed to react in time"
    # Level-4
        self.attack7 = self.fourth_level_focus
        self.attack7_descrip = "8.) Focused Strike - extra precise hit"
        self.attack7_fail = "overfocused and missed"
        self.attack8 = self.shadow_strike
        self.attack8_descrip = "9.) Shadow Strike - bonus damage from darkness"
        self.attack8_fail = "couldn't vanish into shadows"
    # Level-5
        self.attack9 = self.death_blow
        self.attack9_descrip = "10.) Death Blow - massive critical damage"
        self.attack9_fail = "attack was too slow"
        self.attack10 = self.flurry_of_blades
        self.attack10_descrip = "11.) Flurry of Blades - two rapid strikes"
        self.attack10_fail = "blades moved too quickly"

    def rapier_stab(self, target):
        damage = int(round(2 + self.dexterity * random.uniform(0.4, 0.6) + self.strength * random.uniform(0.2, 0.3)))
        target.health -= damage
        print(border)
        print(f"{self.name} stabs {target.name} for {damage} damage")
        print(border)

    def sly_flourish(self, target):
        damage = int(round(1 + self.dexterity * random.uniform(0.3, 0.5) + self.strength * random.uniform(0.2, 0.3)))
        target.health -= damage
        print(border)
        print(f"{self.name} flourishes {target.name} for {damage} damage")
        print(border)

    def healing_potion(self):
        heals = round(10 + random.uniform(2, 4))
        self.health += heals
        print(f"{self.name} drinks a potion and heals for {heals}")
        print(f"{self.name}'s health is now {self.health}")

    def counter_attack(self, target):
        attack = random.choice([self.rapier_stab, self.sly_flourish])
        attack(target)

    # Level-2
    def sneak_attack(self, target):
        bonus = int(round(self.dexterity * random.uniform(0.5, 0.7)))
        target.health -= bonus
        print(f"{self.name} performs Sneak Attack for {bonus} bonus damage!")

    def cunning_dash(self, _=None):
        print(f"{self.name} dashes to a new position!")

    # Level-3
    def evade(self, _=None):
        self.evading = True
        print(f"{self.name} is ready to dodge incoming area effects!")

    def uncanny_dodge(self, damage):
        reduced = damage // 2
        print(f"{self.name} halves incoming damage from {damage} to {reduced}!")
        return reduced

    # Level-4
    def fourth_level_focus(self, target):
        damage = int(round(3 + self.dexterity * 0.6))
        target.health -= damage
        print(f"{self.name} lands a Focused Strike for {damage} damage!")

    def shadow_strike(self, target):
        damage = int(round(2 + self.dexterity * random.uniform(0.4, 0.6)))
        target.health -= damage
        print(f"{self.name} strikes from the shadows for {damage} damage!")

    # Level-5
    def death_blow(self, target):
        damage = int(round(5 + self.strength * random.uniform(0.5, 0.8)))
        target.health -= damage
        print(f"{self.name} executes Death Blow for {damage} damage!")

    def flurry_of_blades(self, target):
        hits = 2
        total = 0
        for _ in range(hits):
            dmg = int(round(1 + self.dexterity * random.uniform(0.3, 0.5)))
            total += dmg
        target.health -= total
        print(f"{self.name} unleashes Flurry of Blades for {total} total damage!")


class Ranger(DND_CLASS):
    def __init__(self, name, health, intelligence, wisdom, dexterity, strength, arrows, xp, level=1, inventory=None):
        super().__init__(name, health, intelligence, wisdom, dexterity, strength, xp, level, inventory)
        self.arrows = arrows
        self.attack1 = self.bow_shot
        self.attack1_descrip = "1.) Bow Shot - moderate pierce damage"
        self.attack1_fail = f"{self.name} missed the arrow!"
        self.attack2 = self.basic_melee
        self.attack2_descrip = "2.) Basic Melee - light slash damage"
        self.attack2_fail = f"{self.name} missed their melee swing!"
        self.heal1 = self.healing_potion
        self.heal1_descrip = "3.) Healing Potion - restores a small amount of health"
        self.counter = self.counter_attack

    # Level-2
        self.attack3 = self.cast_hunters_mark
        self.attack3_descrip = "4.) Hunter's Mark - mark target for bonus damage"
        self.attack3_fail = "failed to mark target"
        self.attack4 = self.summon_beast
        self.attack4_descrip = "5.) Summon Beast - your animal companion assists"
        self.attack4_fail = "companion failed to appear"

    # Level-3
        self.attack5 = self.spike_growth
        self.attack5_descrip = "6.) Spike Growth - area damage over time"
        self.attack5_fail = "spikes don't appear"
        self.attack6 = self.horde_breaker
        self.attack6_descrip = "7.) Horde Breaker - extra arrow against another target"
        self.attack6_fail = "no secondary target"

    # Level-4
        self.attack7 = self.volley_shot
        self.attack7_descrip = "8.) Volley - fire arrows at multiple foes"
        self.attack7_fail = "arrows scatter harmlessly"
        self.attack8 = self.freedom_of_movement
        self.attack8_descrip = "9.) Freedom of Movement - ignore difficult terrain"
        self.attack8_fail = "movement hampered"

    # Level-5
        self.attack9 = self.steel_wind_strike
        self.attack9_descrip = "10.) Steel Wind Strike - teleport and strike"
        self.attack9_fail = "failed to teleport"
        self.attack10 = self.conjure_barrage
        self.attack10_descrip = "11.) Conjure Barrage - rain of arrows"
        self.attack10_fail = "rain of arrows fumbles"

    def bow_shot(self, target):
        if self.arrows <= 0:
            print("No arrows left!")
            return self.basic_melee(target)
        self.arrows -= 1
        damage = int(round(2 + self.dexterity * random.uniform(0.4, 0.6) + 0.3 * self.strength))
        target.health -= damage
        print(border)
        print(f"{self.name} fires an arrow for {damage} damage – arrows left: {self.arrows}")
        print(border)

    def attack1_fail(self):
        print(f"{self.name}'s vision was impaired and the arrow missed.")

    def basic_melee(self, target):
        damage = int(round(1 + self.dexterity * random.uniform(0.3, 0.5) + 0.2 * self.strength))
        target.health -= damage
        print(border)
        print(f"{self.name} slashes for {damage} damage")
        print(border)

    def healing_potion(self):
        heals = round(10 + random.uniform(2, 4))
        self.health += heals
        print(f"{self.name} heals for {heals} -health is now {self.health}")

    def counter_attack(self, target):
        attack = random.choice([self.bow_shot, self.basic_melee])
        if attack == self.bow_shot and self.arrows <= 0:
            return self.basic_melee(target)
        return attack(target)

    # Level-2
    def cast_hunters_mark(self, target):
        self.hunted = target
        print(f"{self.name} marks {target.name}, dealing extra damage on hits!")

    def summon_beast(self, target):
        print(f"{self.name}’s beast companion lunges at {target.name}!")

    # Level-3
    def spike_growth(self, targets):
        print(f"{self.name} summons spiky terrain - foes take damage each turn!")

    def horde_breaker(self, target):
        extra = int(round(self.dexterity * 0.5))
        target.health -= extra
        print(f"{self.name} fires at an additional target for {extra} damage!")

    # Level-4
    def volley_shot(self, targets):
        print(f"{self.name} unleashes a volley at multiple enemies!")

    def freedom_of_movement(self, _=None):
        self.free_move = True
        print(f"{self.name} can ignore difficult terrain!")

    # Level-5
    def steel_wind_strike(self, target):
        damage = int(round(3 + self.strength * random.uniform(0.3, 0.5)))
        target.health -= damage
        print(f"{self.name} teleports and strikes {target.name} for {damage} damage!")

    def conjure_barrage(self, targets):
        print(f"{self.name} rains arrows down on all enemies!")


class Barbarian(DND_CLASS):
    def __init__(self, name, health, intelligence, wisdom, dexterity, strength, xp, level=1, inventory=None):
        super().__init__(name, health, intelligence, wisdom, dexterity, strength, xp, level, inventory)
        self.attack1 = self.raging_strike
        self.attack1_descrip = "1.) Raging Strike - heavy melee damage"
        self.attack1_fail = f"{self.name} swings wildly and misses!"
        self.attack2 = self.reckless_swing
        self.attack2_descrip = "2.) Reckless Swing - light melee damage"
        self.attack2_fail = f"{self.name}'s reckless swing misses!"
        self.heal1 = self.healing_potion
        self.heal1_descrip = "3.) Healing Potion - restores moderate health"
        self.counter = self.counter_attack

    # Level-2
        self.attack3 = self.reckless_attack
        self.attack3_descrip = "4.) Reckless Attack - advantage on melee but vulnerable"
        self.attack3_fail = "attack lacked focus"
        self.attack4 = self.danger_sense
        self.attack4_descrip = "5.) Danger Sense - advantage on Dex saves"
        self.attack4_fail = "couldn't sense danger"

    # Level-3
        self.attack5 = self.frenzy
        self.attack5_descrip = "6.) Frenzy - bonus attack on each turn"
        self.attack5_fail = "rage subsides too quickly"
        self.attack6 = self.mindless_rage
        self.attack6_descrip = "7.) Mindless Rage - immune to charm/fear"
        self.attack6_fail = "rage unsettled"

    # Level-4
        self.attack7 = self.brutal_critical
        self.attack7_descrip = "8.) Brutal Critical - extra weapon die on crit"
        self.attack7_fail = "bladed edge dulls"
        self.attack8 = self.retaliation
        self.attack8_descrip = "9.) Retaliation - attack back when hit"
        self.attack8_fail = "reaction was slow"

    # Level-5
        self.attack9 = self.relentless_rage
        self.attack9_descrip = "10.) Relentless Rage - stay standing at 0 HP"
        self.attack9_fail = "fatigue takes over"
        self.attack10 = self.persistent_rage
        self.attack10_descrip = "11.) Persistent Rage - rage ends only on rest"
        self.attack10_fail = "rage flickers out"

    def raging_strike(self, target):
        damage = int(round(4 + self.strength * random.uniform(0.5, 0.8)))
        target.health -= damage
        print(border)
        print(f"{self.name} unleashes Raging Strike for {damage} damage")
        print(border)

    def reckless_swing(self, target):
        damage = int(round(2 + self.strength * random.uniform(0.3, 0.5) + self.dexterity * random.uniform(0.2, 0.3)))
        target.health -= damage
        print(border)
        print(f"{self.name} performs Reckless Swing for {damage} damage")
        print(border)

    def healing_potion(self):
        heals = int(round(8 + self.strength * 0.5 + random.uniform(2, 6)))
        self.health += heals
        print(f"{self.name} heals for {heals} - health is now {self.health}")

    def counter_attack(self, target):
        attack = random.choice([self.raging_strike, self.reckless_swing])
        attack(target)

    # Level-2
    def reckless_attack(self, target):
        print(f"{self.name} attacks with reckless abandon!")

    def danger_sense(self, _=None):
        self.adv_on_dex = True
        print(f"{self.name} can sense danger and gains advantage on Dexterity saves!")

    # Level-3
    def frenzy(self, target):
        extra = int(round(self.strength * 0.3))
        target.health -= extra
        print(f"{self.name} enters Frenzy and strikes for extra {extra} damage!")

    def mindless_rage(self, _=None):
        print(f"{self.name} is immune to charm and fear while raging!")

    # Level-4
    def brutal_critical(self, target):
        bonus_die = random.randint(1, 6)
        target.health -= bonus_die
        print(f"{self.name} scores Brutal Critical adding {bonus_die} damage!")

    def retaliation(self, target):
        print(f"{self.name} retaliates against the foe!")

    # Level-5
    def relentless_rage(self, _=None):
        print(f"{self.name} can stay standing at 0 HP once per rage!")

    def persistent_rage(self, _=None):
        print(f"{self.name}'s rage will only end on a long rest!")


class Fighter(DND_CLASS):
    def __init__(self, name, health, intelligence, wisdom, dexterity, strength, xp, level=1, inventory=None):
        super().__init__(name, health, intelligence, wisdom, dexterity, strength, xp, level, inventory)
        self.attack1 = self.power_thrust
        self.attack1_descrip = "1.) Power Thrust - heavy melee damage"
        self.attack1_fail = f"{self.name}'s power thrust misses!"
        self.attack2 = self.quick_slash
        self.attack2_descrip = "2.) Quick Slash - light melee damage"
        self.attack2_fail = f"{self.name}'s quick slash misses!"
        self.heal1 = self.healing_potion
        self.heal1_descrip = "3.) Second Wind - regain health once per short rest"
        self.counter = self.counter_attack

    # Level-2
        self.attack3 = self.second_wind
        self.attack3_descrip = "4.) Second Wind - self-heal mid-combat"
        self.attack3_fail = "too exhausted to recover"
        self.attack4 = self.action_surge
        self.attack4_descrip = "5.) Action Surge - take an extra action"
        self.attack4_fail = "lungs fail to surge"

    # Level-3
        self.attack5 = self.extra_attack
        self.attack5_descrip = "6.) Extra Attack - attack twice"
        self.attack5_fail = "miss both swings"
        self.attack6 = self.parry
        self.attack6_descrip = "7.) Parry - reduce damage from one hit"
        self.attack6_fail = "failed to parry"

    # Level-4
        self.attack7 = self.indomitable
        self.attack7_descrip = "8.) Indomitable - reroll a saving throw"
        self.attack7_fail = "luck ran out"
        self.attack8 = self.improved_critical
        self.attack8_descrip = "9.) Improved Critical - crit on 19-20"
        self.attack8_fail = "critical edge dulls"

    # Level-5
        self.attack9 = self.supreme_strike
        self.attack9_descrip = "10.) Supreme Strike - heavy precision damage"
        self.attack9_fail = "strike lacked focus"
        self.attack10 = self.battle_mastery
        self.attack10_descrip = "11.) Battle Mastery - choose a combat superiority"
        self.attack10_fail = "mastery slips away"

    def power_thrust(self, target):
        damage = int(round(4 + 0.5 * self.strength + 0.3 * self.dexterity))
        target.health -= damage
        print(border)
        print(f"{self.name} delivers Power Thrust for {damage} damage")
        print(border)

    def quick_slash(self, target):
        damage = int(round(1 + self.dexterity * random.uniform(0.3, 0.5) + self.strength * random.uniform(0.2, 0.3)))
        target.health -= damage
        print(border)
        print(f"{self.name} lands Quick Slash for {damage} damage")
        print(border)

    def healing_potion(self):
        heals = int(round(7 + self.wisdom * 0.5 + random.uniform(2, 5)))
        self.health += heals
        print(f"{self.name} uses Second Wind and recovers {heals} health!")
        print(f"{self.name}'s health is now {self.health}")

    def counter_attack(self, target):
        attack = random.choice([self.power_thrust, self.quick_slash])
        attack(target)

    # Level-2
    def second_wind(self, _=None):
        heals = int(round(10 + self.wisdom * 0.3))
        self.health += heals
        print(f"{self.name} uses Second Wind to heal {heals}!")

    def action_surge(self, _=None):
        print(f"{self.name} surges with energy and gains an extra action!")

    # Level-3
    def extra_attack(self, target):
        print(f"{self.name} attacks twice!")
        self.power_thrust(target)
        self.quick_slash(target)

    def parry(self, damage):
        reduced = damage - int(self.dexterity * 0.2)
        print(f"{self.name} parries and reduces damage to {reduced}!")
        return reduced

    # Level-4
    def indomitable(self, _=None):
        print(f"{self.name} rerolls a failed saving throw!")

    def improved_critical(self, target):
        crit_dmg = random.randint(1, 8) + int(self.strength * 0.2)
        target.health -= crit_dmg
        print(f"{self.name} scores Improved Critical for {crit_dmg} damage!")

    # Level-5
    def supreme_strike(self, target):
        damage = int(round(6 + self.strength * 0.5))
        target.health -= damage
        print(f"{self.name} lands Supreme Strike for {damage} damage!")

    def battle_mastery(self, _=None):
        print(f"{self.name} chooses a Battle Mastery maneuver!")


class Paladin(DND_CLASS):
    def __init__(self, name, health, intelligence, wisdom, dexterity, strength, xp, level=1, inventory=None):
        super().__init__(name, health, intelligence, wisdom, dexterity, strength, xp, level, inventory)
        self.attack1 = self.divine_smite
        self.attack1_descrip = "1.) Divine Smite - heavy radiant damage"
        self.attack1_fail = f"{self.name}'s smite misses!"
        self.attack2 = self.radiant_strike
        self.attack2_descrip = "2.) Radiant Strike - light radiant damage"
        self.attack2_fail = f"{self.name}'s strike misses!"
        self.heal1 = self.healing_potion
        self.heal1_descrip = "3.) Lay on Hands - restore moderate health"
        self.counter = self.counter_attack

    # Level-2
        self.attack3 = self.lay_on_hands
        self.attack3_descrip = "4.) Lay on Hands - heal yourself or ally"
        self.attack3_fail = "hands tremble under strain"
        self.attack4 = self.oath_protection
        self.attack4_descrip = "5.) Oath of Protection - shield ally"
        self.attack4_fail = "oath power falters"

    # Level-3
        self.attack5 = self.divine_health
        self.attack5_descrip = "6.) Divine Health - immunity to disease"
        self.attack5_fail = "faith wavers"
        self.attack6 = self.aura_of_protection
        self.attack6_descrip = "7.) Aura of Protection - add Cha to saves"
        self.attack6_fail = "aura flickers"

    # Level-4
        self.attack7 = self.cleansing_touch
        self.attack7_descrip = "8.) Cleansing Touch - end a condition"
        self.attack7_fail = "touch lacks power"
        self.attack8 = self.aura_of_courage
        self.attack8_descrip = "9.) Aura of Courage - immunity to fear"
        self.attack8_fail = "aura wavers"

    # Level-5
        self.attack9 = self.extra_attack
        self.attack9_descrip = "10.) Extra Attack - attack twice"
        self.attack9_fail = "miss both strikes"
        self.attack10 = self.holy_wrath
        self.attack10_descrip = "11.) Holy Wrath - radiant blast"
        self.attack10_fail = "wrath dims"

    def divine_smite(self, target):
        damage = int(round(4 + 0.5 * self.strength + 0.3 * self.wisdom))
        target.health -= damage
        print(border)
        print(f"{self.name} calls Divine Smite for {damage} damage")
        print(border)

    def radiant_strike(self, target):
        damage = int(round(1 + self.strength * random.uniform(0.2, 0.3) + self.dexterity * random.uniform(0.2, 0.3)))
        target.health -= damage
        print(border)
        print(f"{self.name} delivers Radiant Strike for {damage} damage")
        print(border)

    def healing_potion(self):
        heals = int(round(3 + self.wisdom + random.uniform(3, 5)))
        self.health += heals
        print(f"{self.name} uses Lay on Hands for {heals} health!")
        print(f"{self.name}'s health is now {self.health}")

    def counter_attack(self, target):
        attack = random.choice([self.divine_smite, self.radiant_strike])
        attack(target)

    # Level-2
    def lay_on_hands(self, target=None):
        heals = int(round(10 + self.level * 2))
        if target:
            target.health += heals
            print(f"{self.name} heals {target.name} for {heals} health!")
        else:
            self.health += heals
            print(f"{self.name} heals themselves for {heals} health!")

    def oath_protection(self, target):
        target.protected = True
        print(f"{self.name} shields {target.name} with Oath Protection!")

    # Level-3
    def divine_health(self, _=None):
        self.immune_to_disease = True
        print(f"{self.name} is now immune to disease!")

    def aura_of_protection(self, _=None):
        self.aura_buff = True
        print(f"{self.name} grants Aura of Protection - add CHA to saves!")

    # Level-4
    def cleansing_touch(self, target):
        if hasattr(target, 'condition'):
            del target.condition
            print(f"{self.name} cleanses {target.name}'s condition!")
        else:
            print("No condition to remove.")

    def aura_of_courage(self, _=None):
        self.fear_immunity = True
        print(f"{self.name} and nearby allies are immune to fear!")

    # Level-5
    def extra_attack(self, target):
        print(f"{self.name} attacks twice!")
        self.divine_smite(target)
        self.radiant_strike(target)

    def holy_wrath(self, targets):
        damage = sum(random.randint(1, 6) for _ in range(3)) + int(self.wisdom * 0.3)
        print(border)
        print(f"{self.name} unleashes Holy Wrath for {damage} radiant damage!")
        for tgt in targets:
            tgt.health -= damage
            print(f"  – {tgt.name}'s health is now {tgt.health}")
        print(border)



class Boss(DND_CLASS):
   #Bosses start at level 4, because Boss.
    def __init__(self,name,health,intelligence,wisdom,dexterity,strength,xp,level=4,inventory=None):
        super().__init__(name, health, intelligence, wisdom, dexterity, strength, xp, level, inventory)
       
        self.attack1 = self.basic_attack
        self.attack1_descrip = f"A basic slashing attack."

        self.attack2 = self.heavy_attack
        self.attack2_descrip = (f"A heavy crushing blow -deals heavy bludegoning damage.")

    def heavy_attack(self, target):
        rolls = [random.randint(1, 6) for _ in range(2)]
        damage = sum(rolls) + self.strength + self.level
        target.health -= damage
        
    def basic_attack(self, target):
        damage = random.randint(1, 4) + self.strength
        target.health -= damage
        
    def counter_attack(self, target):
        attack = random.choice([self.heavy_attack, self.basic_attack])
        attack(target)


class Enemy(DND_CLASS):
    def __init__(self, name, health, intelligence, wisdom, dexterity, strength, xp, level =1 , inventory=None):
        super().__init__(name, health, intelligence, wisdom, dexterity, strength, xp, level, inventory)
        self.attack1 = self.basic_attack
        self.attack1_descrip = "A basic slashing attack." 
        self.counter = self.counter_attack
        
        
    @staticmethod
    def enemy_name_and_stats():
        total_enemies = random.randint(20, 30)
        possible_names = [
    "Goblin", "Orc", "Skeleton", "Zombie", "Bandit", "Giant Rat", "Giant Spider", "Slime", "Wolf", "Troll",
    "Vampire", "Ghost", "Cultist", "Dark Mage", "Kobold", "Lizardman", "Imp", "Ogre", "Harpy", "Wraith",
    "Mimic", "Bat", "Bugbear", "Gnoll", "Shadow", "Gargoyle", "Werewolf", "Sorcerer", "Assassin", "Elemental",
    "Hobgoblin", "Banshee", "Basilisk", "Chimera", "Drider", "Ettercap", "Ghoul", "Hag", "Hydra", "Lamia",
    "Manticore", "Medusa", "Minotaur", "Myconid", "Otyugh", "Quasit", "Rakshasa", "Sahuagin", "Specter", "Yuan-ti"
]
        enemies_for_encounter = []
        for _ in range(total_enemies):
            name = random.choice(possible_names)
            health = random.randint(12, 18)           
            intelligence = random.randint(1, 3)
            wisdom = random.randint(1, 3)
            dexterity = random.randint(1, 3)
            strength = random.randint(1, 3)
            xp = random.randint(3, 8)
            level = 1
            inventory = None
            final_enemy = Enemy(name, health, intelligence, wisdom, dexterity, strength, xp, level, inventory)
            enemies_for_encounter.append(final_enemy)
        return enemies_for_encounter
    
    def create_class_variables(self):
        self.vars = dict(self.__dict__)
        return self.vars
    
    def basic_attack(self, target):
        """Weaker NPC attack: small base + light stat scaling + minor randomness"""
        damage = int(round(
            2 + self.strength * random.uniform(0.3, 0.5)
            + self.dexterity * random.uniform(0.2, 0.4)
            + random.uniform(0, 1)
        ))
        target.health -= damage
        print(f"{self.name} attacks {target.name} for {damage} damage!")
        if target.health <= 0:
            print(f"{target.name} has been defeated!")
        else:
            print(f"{target.name}'s health is now {target.health}")

    def counter_attack(self, target):
        # NPCs simply use their basic attack when countering
        self.basic_attack(target)

class Room:
    def __init__ (self, description, exits, characters, visited, secret = None, items=None):
        self.description = description
        self.exits = exits
        self.items = items if items is not None else []
        self.characters = characters
        self.visited = visited
        self.secret = secret if secret is not None else {}


    def __str__(self):
        return self.description
    
    
    def loot_item(self, character, item):
        self.items.remove(item)
        if isinstance(character, Ranger):
            if item == "arrow":
                character.arrows += 1
                print(f"{character.name} now has {character.arrows} arrows!")
        else:
            if item in character.inventory:
                character.inventory[item] += 1
            else:
                character.inventory[item] = 1 
            if item =="goldfish":
                print(f"You have caught the elusive {item}, are you proud of yourself?!\n")
            else:
                print(f"You looted the {item}!\n")

    def randomize_items_in_rooms(self, item_list, n=3):
         self.items = random.sample(item_list, n)
         
                    
    def randomize_room_descriptions(self, room_descriptions):
            room_description = random.choice(room_descriptions)
            self.description = room_description
            
    def random_npc_drops(self):
        character_drops = ["bloody bandage","crystal key", "torn cloak", "healing potion", "mysterious locket", "engraved dog tag", "worn diary", "silver tooth", "broken spectacles", "family crest ring", "old photograph", "strange coin", "war medal", "faded love letter", "bone charm", "lucky rabbit's foot", "pocket watch", "crumpled wanted poster", "empty flask", "singed feather", "carved bone dice", "embroidered handkerchief"]
        items_dead_will_drop = random.sample(character_drops, 2)
        self.items.extend(items_dead_will_drop)
        return items_dead_will_drop
    
    
    @staticmethod
    def dungeon_room_randomizer(character_list, player, secret_room_mapping,boss_rooms):  # This will be how a random dungeon is generated each time.
        room_count = random.randint(10, 45)
        scenario_room_list = []

        for _ in range(room_count):
            description = ""
            exits = {}  # Set later
            characters = None
            visited = False
            secret = {}
            items = []
            dung_room = Room(description, exits, characters, visited, secret, items)
            scenario_room_list.append(dung_room)

        rooms_populated = random.sample(scenario_room_list, random.randint(10, room_count))
        rooms_with_secrets = random.sample(scenario_room_list, random.randint(4, room_count))  ##random.randint(4, room_count)
        scenario_room_list.extend(boss_rooms)
        
        
        for room in rooms_populated:
            character_options = []
            for character in character_list:
                if character != player:
                    character_options.append(character)
            enemies_for_encounter = Enemy.enemy_name_and_stats()
            enemy_mapping = {}
            character_in_room = random.choice(character_options)
            npcs_in_room = random.sample(enemies_for_encounter, 3)
            combined_enemy_list = [character_in_room] + npcs_in_room
            for enemy in combined_enemy_list:
                enemy_mapping[enemy.name] = enemy
            room.characters = enemy_mapping
            
        for room in rooms_with_secrets:
            if room in boss_rooms:
                continue
            key, value = random.choice(list(secret_room_mapping.items()))
            room.secret[key] = value
            
            
        
        reverse_direction = {
            "north": "south",
            "south": "north",
            "east": "west",
            "west": "east"
        }

        directions = ["north", "south", "east", "west"]

        for room in scenario_room_list:
            possible_destinations = [r for r in scenario_room_list if r is not room]
            if not possible_destinations:
                continue  # Prevents crash if 0 rooms exits available 
            num_exits = random.randint(1, min(3, len(possible_destinations)))
            chosen_directions = random.sample(directions, num_exits)
            chosen_rooms = random.sample(possible_destinations, num_exits)
            for direction, dest_room in zip(chosen_directions, chosen_rooms):
                room.exits[direction] = dest_room
                rev_dir = reverse_direction[direction]
                if rev_dir not in dest_room.exits:
                    dest_room.exits[rev_dir] = room
                    
                    
                    
        #Secret room, maybe add perception check into exploration to look for secret mechanisms that will allow for secret room access 

        
        
        
        return scenario_room_list



