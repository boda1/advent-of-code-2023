with open('./input.txt') as f:
    numbers_text = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    calibration_sum = 0
    for line in f.read().split('\n'):
        print(line)
        if line.isalpha():
            all_matches = sorted({line.find(number): number for number in numbers_text if number in line}.items())
            x = numbers_text.index(all_matches[0][1]) + 1
            y = numbers_text.index(all_matches[len(all_matches) - 1][1]) + 1
            print(x, y)
        else:
            all_matches = sorted({line.find(number): number for number in numbers_text if number in line}.items())

            for char in line:
                if char.isnumeric():
                    if any(number in line.split(char)[0] for number in numbers):
                        all_matches = sorted({line.find(number): number for number in numbers if number in line}.items())
                        x_index_word = numbers.index(all_matches[0][1])
                        if line.index(char) < x_index_word:
                            x = char
                        else:
                            x = numbers.index(all_matches[0][1]) + 1
                    else:
                        x = char
                    if any(number in line.split(char)[1] for number in numbers):
                        half_of_line = line.split(char, 1)[1]
                        all_matches = sorted({line.find(number): number for number in numbers if number in line}.items())
                        print(all_matches)
                        y_index_of_last_word = all_matches[len(all_matches) - 1][0]
                        print(y_index_of_last_word)

                        y_index_of_last_number = 0
                        for i in range(len(half_of_line) - 1, -1, -1):
                            if half_of_line[i].isnumeric():
                                y_index_of_last_number = i
                                break

                        if y_index_of_last_word > y_index_of_last_number:
                            y = numbers.index(all_matches[len(all_matches) - 1][1]) + 1
                        else:
                            y = half_of_line[y_index_of_last_number]
                    else:
                        for i in range(len(line) - 1, -1, -1):
                            if line[i].isnumeric():
                                y = line[i]
                                break
                    break
        print(x, y)
        num_to_add = str(x) + str(y)
        calibration_sum += int(num_to_add)
        print(calibration_sum)
