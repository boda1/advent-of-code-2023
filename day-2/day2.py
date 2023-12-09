with open('./input.txt') as f:
    max_cubes = {'red': 12, 'green': 13, 'blue': 14}
    game_id_sum = 0
    for line in f.read().split('\n'):
        game_id = line.split(':')[0].split(' ')[1]
        all_hands_in_game = line.split(':')[1]
        valid_game = True

        for hand in all_hands_in_game.split(';'):
            hand_dict = {colour.split(' ')[2]: colour.split(' ')[1] for colour in hand.split(',')}

            if any(int(hand_dict[key]) > int(max_cubes[key]) for key in hand_dict):
                print("not valid!")
                valid_game = False
            else:
                print("valid!")

        if valid_game:
            game_id_sum += int(game_id)

        print(game_id_sum)


