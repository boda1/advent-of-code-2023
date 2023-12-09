with open('../day-4/input.txt') as f:
    lines = f.read().split('\n')
    total_points = 0

    for line in lines:
        no_winning_numbers = 0
        points_from_card = 0
        winning_numbers = list(filter(lambda x: x != '', line.split('|')[0].split(':')[1].split(' ')))
        my_numbers = list(filter(lambda x: x != '', line.split('|')[1].split(' ')))

        for number in my_numbers:
            if number in winning_numbers:
                no_winning_numbers += 1

        if no_winning_numbers == 1:
            points = 1
        elif no_winning_numbers > 1:
            points = pow(2, no_winning_numbers - 1)
        else:
            points = 0
        print(line, points)

        total_points += points

    print(total_points)
