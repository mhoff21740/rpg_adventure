import random

boarder = "=" * 70


def randomize_character_spawn(rooms_list,target):
        room_choise = random.choice(rooms_list)
        room_choise.characters = target
        
def randomize_items_in_rooms(item_list ,rooms_list):
        for room in rooms_list:
                room_items = random.sample(item_list, 4)
                room.items= room_items
                
        