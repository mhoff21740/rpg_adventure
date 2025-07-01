
""" ########################################## BACK UP INCASE MY LEVELING SYSTEM NO WORK###########################################################



import random
from constants_and_utlility_funcs import border




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
        self.inventory = inventory if inventory is not None else {}
        

    def create_class_variable(self): # Used for the bugging of the de. 
        self.vars = {
            key: value
            for key, value in self.__dict__.items()
            if not callable(value)
        }
        return self.vars

    
    
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
            if self.level // 2 != 0 and self.level >= 3:
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
            print(f"{self.name} now has {self.xp} XP (Level {self.level})")
    
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
        


# Rebalanced level-1 damage formulas for each class

class Wizard(DND_CLASS):
    def __init__(self, name, health, intelligence, wisdom, dexterity, strength, xp, level=1, inventory=None):
        super().__init__(name, health, intelligence, wisdom, dexterity, strength, xp, level, inventory)
        self.attack1 = self.cast_firebolt
        self.attack1_descrip = "1.)Cast Firebolt - deals moderate fire damage" 
        self.attack1_fail = "accidentally launched a fireball over"
        self.attack2 = self.cast_ice_shard
        self.attack2_descrip ="2.) Cast Ice Shard - deals light cold damage."
        self.attack2_fail = "accidentally launched an ice shard over"
        self.heal1 = self.healing_word
        self.heal1_descrip =  "3.) Cast Healing Word - restores a small amount of health."
        self.counter = self.counter_attack
        
    def cast_firebolt(self, target):
        # Level-1 fireball: lower base, scaled by stats
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
        # Level-1 ice shard: even lighter
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
        heals = round(6 + (self.wisdom * random.uniform(1, 4)))
        self.health += heals
        print(f"{self.name} has been healed for {heals}!")
        print(f"{self.name}'s health is now {self.health}")

    def counter_attack(self, target):
        attack = random.choice([self.cast_fireball, self.cast_ice_shard])
        attack(target)
        
    def create_class_variables(self):
        self.vars = dict(self.__dict__)
        return self.vars


class Rogue(DND_CLASS):
    def __init__(self, name, health, intelligence, wisdom, dexterity, strength, xp, level=1, inventory=None):
        super().__init__(name, health, intelligence, wisdom, dexterity, strength, xp, level, inventory)
        self.attack1 = self.rapier_stab
        self.attack1_descrip = "1.) Stab with your rapier - deals moderate stab damage."
        self.attack1_fail = "accidetally stabbed the air!"
        self.attack2 = self.sly_flurish
        self.attack2_descrip = "2.) Sly Flurish - deals light stab damage."
        self.attack2_fail = "couldn't sneak up on!"
        self.heal1 = self.healing_potion
        self.heal1_descrip =  "3.) Drink a healing potion - restores a small amount of health"
        self.counter = self.counter_attack
        
    def rapier_stab(self, target):
        # Level-1 stab: focused on dexterity
        damage = int(round(2 + self.dexterity * random.uniform(0.4, 0.6) + self.strength * random.uniform(0.2, 0.3)))
        target.health -= damage
        print(border)
        print(f"{self.name} stabs {target.name} dealing {damage} damage")
        print(border)
        if target.health <= 0:
            print(f"{target.name} has been stabbed to death!\n")
        else:
            print(f"{target.name}'s health is now {target.health}")

    def sly_flurish(self, target):
        # Level-1 flourish: lighter finesse
        damage = int(round(1 + self.dexterity * random.uniform(0.3, 0.5) + self.strength * random.uniform(0.2, 0.3)))
        target.health -= damage
        print(border)
        print(f"{self.name} flourishes {target.name} dealing {damage} damage")
        print(border)
        if target.health <= 0:
            print(f"{target.name} has been flourished to death!\n")
        else:
            print(f"{target.name}'s health is now {target.health}")

    def healing_potion(self):
        heals = round(10 + random.uniform(2, 4))
        self.health += heals
        print(f"{self.name} heals for {heals}")
        print(f"{self.name}'s health is now {self.health}")

    def counter_attack(self, target):
        attack = random.choice([self.rapier_stab, self.sly_flurish])
        attack(target)
    
    def create_class_variables(self):
        self.vars = dict(self.__dict__)
        return self.vars


class Ranger(DND_CLASS):
    def __init__(self, name, health, intelligence, wisdom, dexterity, strength, arrows, xp, level=1, inventory=None):
        super().__init__(name, health, intelligence, wisdom, dexterity, strength, xp, level, inventory)
        self.arrows = arrows
        self.attack1 = self.bow_shot
        self.attack1_descrip = "1.) Bow Shot - deals moderate peirce damage."
        self.attack1_failure = self.attack1_fail
        self.attack2 = self.basic_melee
        self.attack2_descrip ="2.) Basic Melee - deals light slash damage." 
        self.attack2_fail = f"{self.name} has missed"
        self.heal1 = self.healing_potion
        self.heal1_descrip =  "3.) Drink a healing potion - restores a small amount of health"
        self.counter = self.counter_attack

    def bow_shot(self, target):
        if self.arrows <= 0:
            print("Not enough arrows. Resorting to melee.")
            return self.basic_melee(target)
        self.arrows -= 1
        print(f"Arrows left: {self.arrows}")
        damage = int(round(2 + self.dexterity * random.uniform(0.4, 0.6) + 0.3 * self.strength))
        target.health -= damage
        print(border)
        print(f"{self.name} fires an arrow dealing {damage} damage")
        print(border)
        if target.health <= 0:
            print(f"{target.name} has been pierced by an arrow and died!\n")
        else:
            print(f"{target.name}'s health is now {target.health}")

    
    def attack1_fail(self):
        return (
        f"{self.name}'s vision was impaired and he has launched an arrow over the target.\n"
        f"As a result of that blunder, {self.name} now has {self.arrows} arrows"
    )

    
    
    
    def basic_melee(self, target):
        damage = int(round(1 + self.dexterity * random.uniform(0.3, 0.5) + 0.2 * self.strength))
        target.health -= damage
        print(border)
        print(f"{self.name} strikes {target.name} with a melee attack dealing {damage} damage")
        print(border)
        if target.health <= 0:
            print(f"{target.name} has been slashed to death!\n")
        else:
            print(f"{target.name}'s health is now {target.health}")

    def healing_potion(self):
        heals = round(10 + random.uniform(2, 4))
        self.health += heals
        print(f"{self.name} heals for {heals}")
        print(f"{self.name}'s health is now {self.health}")

    def counter_attack(self, target):
        attack = random.choice([self.bow_shot, self.basic_melee])
        if attack == self.bow_shot and self.arrows <= 0:
            print(f"{self.name} has no arrows; using melee counter.")
            return self.basic_melee(target)
        return attack(target)
    
    def create_class_variables(self):
        self.vars = dict(self.__dict__)
        return self.vars


class Barbarian(DND_CLASS):
    def __init__(self, name, health, intelligence, wisdom, dexterity, strength, xp, level=1, inventory=None):
        super().__init__(name, health, intelligence, wisdom, dexterity, strength, xp, level, inventory)
        self.attack1 = self.raging_strike
        self.attack1_descrip = "1.) Raging Strike - deals heavy melee damage."
        self.attack1_fail = f"{self.name} swings wildly and misses their target!"
        self.attack2 = self.reckless_swing
        self.attack2_descrip = "2.) Reckless Swing - deals light melee damage."
        self.attack2_fail = f"{self.name}'s reckless swing misses their target"
        self.heal1 = self.healing_potion
        self.heal1_descrip ="3.) Drink a healing potion - restores a moderate amount of health"
        self.counter = self.counter_attack
        
    def raging_strike(self, target):
        # Level-1 rage: moderate strength scaling
        damage = int(round(4 + self.strength * random.uniform(0.5, 0.8)))
        target.health -= damage
        print(border)
        print(f"{self.name} unleashes Raging Strike dealing {damage} damage!")
        print(border)
        if target.health <= 0:
            print(f"{target.name} has been crushed by might!\n")
        else:
            print(f"{target.name}'s health is now {target.health}")

    def reckless_swing(self, target):
        damage = int(round(2 + self.strength * random.uniform(0.3, 0.5) + self.dexterity * random.uniform(0.2, 0.3)))
        target.health -= damage
        print(border)
        print(f"{self.name} performs Reckless Swing dealing {damage} damage!")
        print(border)
        if target.health <= 0:
            print(f"{target.name} has been felled!\n")
        else:
            print(f"{target.name}'s health is now {target.health}")

    def healing_potion(self):
        heals = int(round(8 + self.strength * 0.5 + random.uniform(2, 6)))
        self.health += heals
        print(f"{self.name} heals for {heals}!")
        print(f"{self.name}'s health is now {self.health}")

    def counter_attack(self, target):
        attack = random.choice([self.raging_strike, self.reckless_swing])
        attack(target)
        
    def create_class_variables(self):
        self.vars = dict(self.__dict__)
        return self.vars


class Fighter(DND_CLASS):
    def __init__(self, name, health, intelligence, wisdom, dexterity, strength, xp, level=1, inventory=None):
        super().__init__(name, health, intelligence, wisdom, dexterity, strength, xp, level, inventory)
        self.attack1 = self.power_thrust
        self.attack1_descrip = "1.) Power Thrust - deals heavy melee damage."
        self.attack1_fail = f"{self.name}'s power thrust misses!"
        self.attack2 = self.quick_slash
        self.attack2_descrip = "2.) Quick Slash - deals light melee damage."
        self.attack2_fail = f"{self.name}'s quick slash misses!"
        self.heal1 = self.healing_potion
        self.heal1_descrip ="3.) Use a healing salve - restores a moderate amount of health"
        self.counter = self.counter_attack
    
    
    
    def power_thrust(self, target):
        # Level-1 thrust: balanced strength and dex
        damage = int(round(4 + 0.5 * self.strength + 0.3 * self.dexterity))
        target.health -= damage
        print(border)
        print(f"{self.name} delivers Power Thrust dealing {damage} damage!")
        print(border)
        if target.health <= 0:
            print(f"{target.name} has been defeated!\n")
        else:
            print(f"{target.name}'s health is now {target.health}")

    def quick_slash(self, target):
        damage = int(round(1 + self.dexterity * random.uniform(0.3, 0.5) + self.strength * random.uniform(0.2, 0.3)))
        target.health -= damage
        print(border)
        print(f"{self.name} lands Quick Slash dealing {damage} damage!")
        print(border)
        if target.health <= 0:
            print(f"{target.name} has been knocked out!\n")
        else:
            print(f"{target.name}'s health is now {target.health}")

    def healing_potion(self):
        heals = int(round(7 + self.wisdom * 0.5 + random.uniform(2, 5)))
        self.health += heals
        print(f"{self.name} uses healing salve for {heals} health!\n")
        print(f"{target.name}'s health is now {self.health}")

    def counter_attack(self, target):
        attack = random.choice([self.power_thrust, self.quick_slash])
        attack(target)
        
    def create_class_variables(self):
        self.vars = dict(self.__dict__)
        return self.vars


class Paladin(DND_CLASS):
    def __init__(self, name, health, intelligence, wisdom, dexterity, strength, xp, level=1, inventory=None):
        super().__init__(name, health, intelligence, wisdom, dexterity, strength, xp, level, inventory)
        self.attack1 = self.divine_smite
        self.attack1_descrip = "1.) Divine Smite - deals heavy radiant damage."
        self.attack1_fail = f"{self.name}'s divine smite misses!"
        self.attack2 = self.radiant_strike
        self.attack2_descrip = "2.) Radiant Strike - deals light radiant damage."
        self.attack2_fail = f"{self.name}'s radiant strike misses!"
        self.heal1 = self.healing_potion
        self.heal1_descrip ="3.) Call upon divine energy - restores a moderate amount of health."
        self.counter = self.counter_attack
    
    
    def divine_smite(self, target):
        # Level-1 smite: moderate scaling
        damage = int(round(4 + 0.5 * self.strength + 0.3 * self.wisdom))
        target.health -= damage
        print(border)
        print(f"{self.name} calls Divine Smite dealing {damage} damage!\n")
        print(border)
        if target.health <= 0:
            print(f"{target.name} has been vanquished by holy might!\n")
        else:
            print(f"{target.name}'s health is now {target.health}")

    def radiant_strike(self, target):
        damage = int(round(1 + self.strength * random.uniform(0.2, 0.3) + self.dexterity * random.uniform(0.2, 0.3)))
        target.health -= damage
        print(border)
        print(f"{self.name} delivers Radiant Strike dealing {damage} damage!")
        print(border)
        if target.health <= 0:
            print(f"{target.name} has fallen to the blade!\n")
        else:
            print(f"{target.name}'s health is now {target.health}")

    def healing_potion(self):
        heals = int(round(3 + self.wisdom + random.uniform(3, 5)))
        self.health += heals
        print(f"{self.name} calls upon divine energy and heals for {heals}!\n")
        print(f"{self.name}'s health is now {self.health}")

    def counter_attack(self, target):
        attack = random.choice([self.divine_smite, self.radiant_strike])
        attack(target)

    def create_class_variables(self):
        self.vars = dict(self.__dict__)
        return self.vars


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
        Weaker NPC attack: small base + light stat scaling + minor randomness
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
    def __init__ (self, description, exits, characters, visited, items=None):
        self.description = description
        self.exits = exits
        self.items = []
        self.characters = characters
        self.visited = visited


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
         self.items = random.sample(item_list, 4)
         
    #@staticmethod keep inscase I bork code and need a fallback
    def randomize_character_spawn(rooms_list,character_list,player):
        enemies_for_encounter = Enemy.enemy_name_and_stats()
        rooms_populated = random.sample(rooms_list, len(rooms_list))
        character_options = []
        for character in character_list:
                if character != player:
                        character_options.append(character)
        for room in rooms_populated:
                enemy_maping = {}
                character_in_room = random.choice(character_options)
                npcs_in_room = random.sample(enemies_for_encounter,3)
                combined_enemy_list = [character_in_room] + npcs_in_room
                for enemy in combined_enemy_list:
                    enemy_maping[enemy.name] = enemy
                room.characters = enemy_maping ## 
                    
    def randomize_room_descriptions(self, room_descriptions):
            room_description = random.choice(room_descriptions)
            self.description = room_description
            
    def random_npc_drops(self):
        character_drops = ["bloody bandage","crystal key", "torn cloak", "healing potion", "mysterious locket", "engraved dog tag", "worn diary", "silver tooth", "broken spectacles", "family crest ring", "old photograph", "strange coin", "war medal", "faded love letter", "bone charm", "lucky rabbit's foot", "pocket watch", "crumpled wanted poster", "empty flask", "singed feather", "carved bone dice", "embroidered handkerchief"]
        items_dead_will_drop = random.sample(character_drops, 2)
        self.items.extend(items_dead_will_drop)
        return items_dead_will_drop
    
    
    @staticmethod
    def dungeon_room_randomizer(character_list):  # This will be how a random dungeon is generated each time.
        room_count = random.randint(10, 25)
        scenario_room_list = []

        for _ in range(room_count):
            description = ""
            exits = {}  # Set later
            characters = None
            visited = False
            items = []
            dung_room = Room(description, exits, characters, visited, items)
            scenario_room_list.append(dung_room)

        rooms_populated = random.sample(scenario_room_list, len(scenario_room_list))
        character_options = []
        for character in character_list:
                if character != character.name:
                        character_options.append(character)
        for room in rooms_populated:
                character_options = []
                for character in character_list:
                    if character != character.name:
                        character_options.append(character)
                enemies_for_encounter = Enemy.enemy_name_and_stats()
                enemy_mapping = {}
                character_in_room = random.choice(character_options)
                npcs_in_room = random.sample(enemies_for_encounter,3)
                combined_enemy_list = [character_in_room] + npcs_in_room
                for enemy in combined_enemy_list:
                    enemy_mapping[enemy.name] = enemy
                room.characters = enemy_mapping
                
        
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

        return scenario_room_list




 ###"""