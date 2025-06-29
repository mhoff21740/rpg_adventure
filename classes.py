import random
from constants_and_utlility_funcs import boarder



# This is a collection of classes that will be used thoughout the land of Faerun. 

class DND_CLASS:
    def __init__(self, name, health, intelligence, wisdom, dexterity, strength, inventory=None):
        self.name = name
        self.health = health
        self.intelligence = intelligence
        self.wisdom = wisdom
        self.dexterity = dexterity
        self.strength = strength
        self.inventory = inventory if inventory is not None else {}





class Wizard(DND_CLASS):
    def __init__(self, name, health, intelligence, wisdom, dexterity, strength, inventory=None):
        super().__init__(name, health, intelligence, wisdom, dexterity, strength, inventory)

    def cast_fireball(self, target): 
        damage = int(round( 10 + self.intelligence + self.wisdom * random.uniform(.65, .85)))
        target.health -= damage
        print(boarder)
        print(f"{self.name} casts fireball dealing {damage} damage")
        print(boarder)
        if target.health <= 0:
            print(f"{target.name} has been made kwispy!")
            return
        else:
            print(f"{target.name}'s health is now {target.health}")
            return
        
    
    def cast_ice_shard(self, target):
        damage = int(round( 5 + self.intelligence + self.wisdom * random.uniform(.55, .65)))
        target.health -= damage
        print(boarder)
        print(f"{self.name} casts fireball dealing {damage} damage")
        print(boarder)
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
        
        


class Rouge(DND_CLASS):
    def __init__(self, name, health, intelligence, wisdom, dexterity, strength, inventory=None):
        super().__init__(name, health, intelligence, wisdom, dexterity, strength, inventory)

    def rapier_stab(self, target):
        stabbie = round(10 + ((self.dexterity + self.strength) * random.uniform(.55,.75)))
        target.health -= stabbie
        print(boarder)
        print(f"{self.name} stabs {target.name} dealing {stabbie} damage")
        print(boarder)
        if target.health <= 0:
            print(f"{target.name} has been stabbed to death!")
            return
        else:
            print(f"{target.name}'s health is now {target.health}")
            return
        
    def sly_flurish(self, target):
        damage = int(round( 5 + self.dexterity + self.strength * random.uniform(.45, .55)))
        target.health -= damage
        print(boarder)
        print(f"{self.name} flurishes {target.name} dealing {damage} damage")
        print(boarder)
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
    def __init__(self, name, health, intelligence, wisdom, dexterity, strength, arrows, inventory=None,):
        super().__init__(name, health, intelligence, wisdom, dexterity, strength, inventory)
        self.arrows = arrows

    def bow_shot(self, target):
        if self.arrows <= 0:
            print ("You do not have enough arrows")
            print(f"{self.name} resorts to melee")
            self.basic_melee(target)
        else:
            self.arrows -= 1
            print(f"You now have {self.arrows} arrows!")
            damage = round(10 + ((self.dexterity + (.5 * self.strength) * random.uniform(.55,.75))))
            target.health -= damage
            if target.health <= 0:
                print(boarder)
                print(f"{target.name} has been peirced by and arrow and got a case of the dead")
                print(boarder)
                return
            else:
                print(f"{target.name}'s health is now {target.health}")
    
    def basic_melee(self, target):
        damage = int(round( 10 + self.dexterity + (.5* self.strength) * random.uniform(.55, .65)))
        target.health -= damage
        print(boarder)
        print(f"{self.name} stabs {target.name} dealing {damage} damage")
        print(boarder)
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
    
    def __init__(self, name, health, intelligence, wisdom, dexterity, strength, inventory=None):
        super().__init__(name, health, intelligence, wisdom, dexterity, strength, inventory)

    def enemy_name_and_stats(self,total_enemies= 3):
        possible_names =["Goblin", "Orc", "Skeleton", "Zombie", "Bandit", "Giant Rat", "Giant Spider", "Slime", "Wolf", "Troll", "Vampire", "Ghost", "Cultist", "Dark Mage", "Kobold", "Lizardman", "Imp", "Ogre", "Harpy", "Wraith", "Mimic", "Bat", "Bugbear", "Gnoll", "Shadow", "Gargoyle", "Werewolf", "Sorcerer", "Assassin", "Elemental"]
        enemies_for_encounter = [] 
        for enemy in range(total_enemies): # Make sure to create an enemy object and then store the OBJECT in the list, not the name and everything 
            name = random.choice(possible_names)
            health = random.uniform(15,35)
            intelligence = random.uniform(2, 5)
            wisdom = random.uniform(2, 5)
            dexterity = random.uniform(2, 5)
            strength = random.uniform(2, 5)
            inventory = None
            final_enemy = Enemy(name, health, intelligence,wisdom, dexterity, strength, inventory)
            enemies_for_encounter.append(final_enemy)
        return enemies_for_encounter
    
    def basic_attack(self, target): # Just weak attacks to help player feel better about themselves as they go along, or to farm xp.
        # Weak attack: base damage plus a little randomness, scaled by strength and dexterity
        damage = int(round(3 + (self.strength * 0.7) + (self.dexterity * 0.3) + random.uniform(0, 2)))
        target.health -= damage
        print(f"{self.name} attacks {target.name} for {damage} damage!")
        if target.health <= 0:
            print(f"{target.name} has been defeated!")
        else:
            print(f"{target.name}'s health is now {target.health}")



class Room:
    def __init__ (self, description, exits, characters, visited, items=None):
        self.description = description
        self.exits = exits
        self.items = items if items is not None else ["key", "bottle", "gold coin"] 
        self.characters = characters
        self.visited = visited


    def loot_item(self, character, item):
        self.items.remove(item)
        if isinstance(character. Ranger):
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
    def randomize_character_spawn(rooms_list,character_list, player):
        rooms_populated = random.sample(rooms_list, 2)
        character_options = []
        for character in character_list:
                if character != player:
                        character_options.append(character)
        for room in rooms_populated:
                character_in_room = random.choice(character_options)
                room.characters = character_in_room

    def randomize_room_descriptions(self, room_descriptions):
            room_description = random.choice(room_descriptions)
            self.description = room_description
            
    def random_npc_drops(self):
        character_drops = ["bloody bandage", "torn cloak", "healing potion" "mysterious locket", "engraved dog tag", "worn diary", "silver tooth", "broken spectacles", "family crest ring", "old photograph", "strange coin", "war medal", "faded love letter", "bone charm", "lucky rabbit's foot", "pocket watch", "crumpled wanted poster", "empty flask", "singed feather", "carved bone dice", "embroidered handkerchief"]
        items_dead_will_drop = random.sample(character_drops, 5)
        self.items.extend(items_dead_will_drop)
        return items_dead_will_drop
    
    @staticmethod
    def dungeon_room_randomizer():  # This will be how a random dungeon is generated each time.
        room_count = random.randint(5, 25)
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
                continue  # Prevents crash if 0 rooms exits avaliable 
            num_exits = random.randint(1, min(3, len(possible_destinations)))
            chosen_directions = random.sample(directions, num_exits)
            chosen_rooms = random.sample(possible_destinations, num_exits)

            for direction, dest_room in zip(chosen_directions, chosen_rooms):
                room.exits[direction] = dest_room
                rev_dir = reverse_direction[direction]
                if rev_dir not in dest_room.exits:
                    dest_room.exits[rev_dir] = room

        return scenario_room_list




