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
                self.arrows -= 1
            else:
                print (f"{self.name} has no arrows and resorts to countering with melee")
                self.basic_melee(target)
        else:
            self.basic_melee(target)
    


    


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
        if item in character.inventory:
            character.inventory[item] += 1
        else:
            character.inventory[item] = 1 
        if item =="goldfish":
            print(f"You have caught the elusive {item}, are you proud of yourself?!\n")
        else:
            print(f"You looted the {item}!\n")
















