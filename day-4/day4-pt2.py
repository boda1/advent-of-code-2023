with open('input.txt') as f:
    lines = f.read().split('\n')
    count_of_cards = [1] * len(lines)

    for i, line in enumerate(lines):
        no_winning_numbers = 0
        no_cards_to_add = 0
        # count_of_cards.append(1)

        winning_numbers = list(filter(lambda x: x != '', line.split('|')[0].split(':')[1].split(' ')))
        my_numbers = list(filter(lambda x: x != '', line.split('|')[1].split(' ')))

        for number in my_numbers:
            if number in winning_numbers:
                no_winning_numbers += 1

        if no_winning_numbers > 0:
            no_cards_to_add = no_winning_numbers
            end_point = i + no_cards_to_add
            for j in range(1, no_winning_numbers + 1):
                count_of_cards[i + j] += 1 * count_of_cards[i]

        print(count_of_cards)

        print(sum(count_of_cards))



