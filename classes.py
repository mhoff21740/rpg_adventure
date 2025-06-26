import random


# This is a collection of classes that will be used thoughout the land of Faerun. 

class Wizard:

    def __init__(self, name, health, intelligence, wisdom):
        self.name = name
        self.health = health
        self.intelligence = intelligence
        self.wisdom = wisdom
        self.inventory = []

    def cast_fireball(self, target): 
        damage = int(round( 10 + self.intelligence + self.wisdom * random.uniform(.65, .85)))
        target.health -= damage
        print("========================================================================")
        print(f"{self.name} casts fireball dealing {damage} damage")
        print("=======================================================================")
        if target.health <= 0:
            print(f"{target.name} has been made kwispy!")
            return
        else:
            print(f"{target.name}'s health is now {target.health}")
            return
        
    
    def cast_ice_shard(self, target):
        damage = int(round( 5 + self.intelligence + self.wisdom * random.uniform(.55, .65)))
        target.health -= damage
        print("========================================================================")
        print(f"{self.name} casts fireball dealing {damage} damage")
        print("=======================================================================")
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
        
        


class Rouge:
    
    def __init__(self, name, health, dexterity, strength):
        self.name = name
        self.health = health
        self.dexterity = dexterity
        self.strength = strength
        self.inventory = []
        

    def rapier_stab(self, target):
        stabbie = round(10 + ((self.dexterity + self.strength) * random.uniform(.55,.75)))
        target.health -= stabbie
        print("========================================================================")
        print(f"{self.name} stabs {target.name} dealing {stabbie} damage")
        print("=======================================================================")
        if target.health <= 0:
            print(f"{target.name} has been stabbed to dealth!")
            return
        else:
            print(f"{target.name}'s health is now {target.health}")
            return
        
    def sly_flurish(self, target):
        damage = int(round( 5 + self.dexterity + self.strength * random.uniform(.45, .55)))
        target.health -= damage
        print("========================================================================")
        print(f"{self.name} flurishes {target.name} dealing {damage} damage")
        print("=======================================================================")
        if target.health <= 0:
            print(f"{target.name} has been stabbed to dealth!")
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
        
        
    

class Room:
    def __init__ (self, description, exits, characters, visited, items=None):
        self.description = description
        self.exits = exits
        self.items = items if items is not None else ["key", "bottle", "gold coin"] 
        self.characters = characters
        self.visited = visited

    def describe_room(self):
        print (f"You enter the {self.name} room, it is very dark.\nYou manage to spot{self.items}.\nAlong with those items, you spot {self.characters}!")
        return 

    def loot_item(self, character, item):
        self.items.remove(item)
        character.inventory.append(item)
        if item =="goldfish":
            print(f"You have caught the {item}!")
        else:
            print(f"You looted the {item}!")
















