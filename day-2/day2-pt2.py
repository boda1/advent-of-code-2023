with open('./input.txt') as f:
    max_cubes = {'red': 12, 'green': 13, 'blue': 14}
    overall_total = 0
    for line in f.read().split('\n'):
        game_id = line.split(':')[0].split(' ')[1]
        all_hands_in_game = line.split(':')[1]
        valid_game = True
        max_hand_dict = {}

        for hand in all_hands_in_game.split(';'):
            current_hand_dict = {colour.split(' ')[2]: colour.split(' ')[1] for colour in hand.split(',')}

            for key in current_hand_dict:
                print(current_hand_dict[key])
                if max_hand_dict.get(key) is None or int(current_hand_dict[key]) > int(max_hand_dict[key]):
                    max_hand_dict[key] = current_hand_dict[key]

        hand_total = 1
        for key in max_hand_dict:
            hand_total *= int(max_hand_dict[key])

        # print(max_hand_dict)
        # print(hand_total)
        overall_total += hand_total
        print(overall_total)


