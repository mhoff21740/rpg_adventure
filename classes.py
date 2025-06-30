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
        
    def total_level_and_xp(self): #Needed? Maybe if player just wants to remember what their level is 
        print(f"You have {self.xp} xp, you are level {self.level}!")
        return self.xp
    
    def gain_xp(self, xp_dropped):
        self.xp += xp_dropped
        new_level = self.current_level()
        if new_level > self.level:
            self.health += random.randint(4,10)
            print(f"Congratulations! {self.name} has reached level {new_level} and your health has increased to {self.hea}!")
            self.level = new_level
            if self.level // 2 == 0 and self.level > 3:
                print("You have now unlocked a random ability point increase!")
                ability_to_increase = input("Which ability would you like to increase: intelligence, wisdom, dexterity, or strength?")
                
                (self.health, self.intelligence, self.wisdom, self.dexterity, self.strength)
                
        else:
            print(f"{self.name} now has {self.xp} XP (Level {self.level})")
        
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
        
   
   
                
        
        
 # """ Work on scaling players up, and enemies to adjust for level of player. Also work on scaling player hp as they level!"""      
    
                
        





class Wizard(DND_CLASS):
    def __init__(self, name, health, intelligence, wisdom, dexterity, strength, xp, level =1, inventory=None):
        super().__init__(name, health, intelligence, wisdom, dexterity, strength,xp, level, inventory)

    def cast_fireball(self, target): 
        damage = int(round( 3 + self.intelligence + self.wisdom * random.uniform(.65, .85)))
        target.health -= damage
        print(border)
        print(f"{self.name} casts fireball dealing {damage} damage")
        print(border)
        if target.health <= 0:
            print(f"{target.name} has been made kwispy!")
            return
        else:
            print(f"{target.name}'s health is now {target.health}")
            return
        
    
    def cast_ice_shard(self, target):
        damage = int(round( 2 + self.intelligence + self.wisdom * random.uniform(.55, .65)))
        target.health -= damage
        print(border)
        print(f"{self.name} casts fireball dealing {damage} damage")
        print(border)
        if target.health <= 0:
            print(f"{target.name} has been frozen!")
            return
        else:
            print(f"{target.name}'s health is now {target.health}")
            return
        
    def healing_word(self):
        heals = round(6 + (self.wisdom * random.uniform(1,4)))
        self.health += heals
        print (f"{self.name} has been healed for {heals}!")
        print(f"{self.name}'s health is now {self.health}")
        return 
    
    def counter_attack(self, target):
        counter_option = [self.cast_fireball, self.cast_ice_shard]
        attack = random.choice(counter_option)
        attack(target)
        
        


class Rogue(DND_CLASS):
    def __init__(self, name, health, intelligence, wisdom, dexterity, strength, xp, level =1, inventory=None):
        super().__init__(name, health, intelligence, wisdom, dexterity, strength, xp, level, inventory)

    def rapier_stab(self, target):
        stabbie = round(3 + ((self.dexterity + self.strength) * random.uniform(.55,.75)))
        target.health -= stabbie
        print(border)
        print(f"{self.name} stabs {target.name} dealing {stabbie} damage")
        print(border)
        if target.health <= 0:
            print(f"{target.name} has been stabbed to death!")
            return
        else:
            print(f"{target.name}'s health is now {target.health}")
            return
        
    def sly_flurish(self, target):
        damage = int(round( 2 + self.dexterity + self.strength * random.uniform(.45, .55)))
        target.health -= damage
        print(border)
        print(f"{self.name} flurishes {target.name} dealing {damage} damage")
        print(border)
        if target.health <= 0:
            print(f"{target.name} has been stabbed to death!")
            return
        else:
            print(f"{target.name}'s health is now {target.health}")
            return

    def healing_potion(self):
        heals = round(10 + random.uniform(2,4))
        self.health += heals
        print (f"{self.name} heals himself for {heals}")
        print(f"{self.name}'s health is now {self.health}")
        return   
    
    def counter_attack(self, target):
        counter_option = [self.rapier_stab, self.sly_flurish]
        attack = random.choice(counter_option)
        attack(target)
        


# Will have a collection of arrows at the start, and will attack based on if arrows in inv, else, resort to Melee, until they pick up some more(if you play them)        
class Ranger(DND_CLASS):
    def __init__(self, name, health, intelligence, wisdom, dexterity, strength, arrows, xp, level= 1, inventory=None,):
        super().__init__(name, health, intelligence, wisdom, dexterity, strength, xp, level, inventory)
        self.arrows = arrows

    def bow_shot(self, target):
        if self.arrows <= 0:
            print ("You do not have enough arrows")
            print(f"{self.name} resorts to melee")
            self.basic_melee(target)
        else:
            self.arrows -= 1
            print(f"You now have {self.arrows} arrows!")
            damage = round(3+ ((self.dexterity + (.5 * self.strength) * random.uniform(.55,.75))))
            target.health -= damage
            if target.health <= 0:
                print(border)
                print(f"{target.name} has been pierced by and arrow and got a case of the dead")
                print(border)
                return
            else:
                print(f"{target.name}'s health is now {target.health}")
    
    def basic_melee(self, target):
        damage = int(round( 2 + self.dexterity + (.5* self.strength) * random.uniform(.55, .65)))
        target.health -= damage
        print(border)
        print(f"{self.name} stabs {target.name} dealing {damage} damage")
        print(border)
        if target.health <= 0:
            print(f"{target.name} has been slashed to death!")
            return
        else:
            print(f"{target.name}'s health is now {target.health}")
            return
        

    def healing_potion(self):
        heals = round(10 + random.uniform(2,4))
        self.health += heals
        print (f"{self.name} heals himself for {heals}")
        print(f"{self.name}'s health is now {self.health}")
        return
        

    def counter_attack(self, target):
        counter_option = [self.bow_shot, self.basic_melee]
        attack_option = random.choice(counter_option)
        if attack_option == self.bow_shot:
            if self.arrows > 0:
                self.bow_shot(target)
            else:
                print (f"{self.name} has no arrows and resorts to countering with melee")
                self.basic_melee(target)
        else:
            attack_option(target)
    

class Enemy(DND_CLASS):
    
    def __init__(self, name, health, intelligence, wisdom, dexterity, strength, xp, level =1 , inventory=None):
        super().__init__(name, health, intelligence, wisdom, dexterity, strength, xp, level, inventory)

    @staticmethod
    def enemy_name_and_stats():
        total_enemies = random.randint(20, 30)
        possible_names =["Goblin", "Orc", "Skeleton", "Zombie", "Bandit", "Giant Rat", "Giant Spider", "Slime", "Wolf", "Troll", "Vampire", "Ghost", "Cultist", "Dark Mage", "Kobold", "Lizardman", "Imp", "Ogre", "Harpy", "Wraith", "Mimic", "Bat", "Bugbear", "Gnoll", "Shadow", "Gargoyle", "Werewolf", "Sorcerer", "Assassin", "Elemental"]
        enemies_for_encounter = [] 
        for enemy in range(total_enemies): # Make sure to create an enemy object and then store the OBJECT in the list, not the name and everything 
            name = random.choice(possible_names)
            health = random.randint(15,35)
            intelligence = random.uniform(2, 5)
            wisdom = random.uniform(2, 5)
            dexterity = random.uniform(2, 5)
            strength = random.uniform(2, 5)
            xp = random.randint(20,45)
            level = 1
            inventory = None
            final_enemy = Enemy(name, health, intelligence,wisdom, dexterity, strength, xp, level, inventory)
            enemies_for_encounter.append(final_enemy)
        return enemies_for_encounter
    
    def basic_attack(self, target): # Just weak attacks to help player feel better about themselves as they go along, or to farm xp.
        # Weak attack: base damage plus a little randomness, scaled by strength and dexterity
        damage = int(round(3 + (self.strength * 0.7) + (self.dexterity * 0.3) + random.randint(0, 2)))
        target.health -= damage
        print(f"{self.name} attacks {target.name} for {damage} damage!")
        if target.health <= 0:
            print(f"{target.name} has been defeated!")
        else:
            print(f"{target.name}'s health is now {target.health}")

    def counter_attack(self, target):
        self.basic_attack(target)

class Room:
    def __init__ (self, description, exits, characters, visited, items=None):
        self.description = description
        self.exits = exits
        self.items = items if items is not None else ["key", "bottle", "gold coin"] 
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

    def randomize_items_in_rooms(self, item_list, n=5):
         self.items = random.sample(item_list, 5)
         
    @staticmethod
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
                room.characters = enemy_maping
                    
    def randomize_room_descriptions(self, room_descriptions):
            room_description = random.choice(room_descriptions)
            self.description = room_description
            
    def random_npc_drops(self):
        character_drops = ["bloody bandage", "torn cloak", "healing potion", "mysterious locket", "engraved dog tag", "worn diary", "silver tooth", "broken spectacles", "family crest ring", "old photograph", "strange coin", "war medal", "faded love letter", "bone charm", "lucky rabbit's foot", "pocket watch", "crumpled wanted poster", "empty flask", "singed feather", "carved bone dice", "embroidered handkerchief"]
        items_dead_will_drop = random.sample(character_drops, 5)
        self.items.extend(items_dead_will_drop)
        return items_dead_will_drop
    
    @staticmethod
    def dungeon_room_randomizer():  # This will be how a random dungeon is generated each time.
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




