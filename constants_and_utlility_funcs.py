boarder = "=" * 70


def randomize_character_spawn(rooms_list,target):
        room_choise = random.choice(rooms_list)
        room_choise.characters = target