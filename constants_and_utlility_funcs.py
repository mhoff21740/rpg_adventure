import random

boarder = "=" * 70



"""Create functions to random all room attributes. Current attributes in rooms:
* Description:
*exits:
*characters: Basic random done
* Visited = Just T or F
*items: Done 

"""



"""maybe these can be methods in the classes, revisit later """


        
def randomize_items_in_rooms(item_list ,rooms_list):
        for room in rooms_list:
                room_items = random.sample(item_list, 5)
                room.items= room_items
                
                

def randomize_character_spawn(rooms_list,character_list, player):
        rooms_populated = random.sample(rooms_list, 2)
        character_options = []
        for character in character_list:
                if character != player:
                        character_options.append(character)
        for room in rooms_populated:
                character_in_room = random.choice(character_options)
                room.characters = character_in_room
                






