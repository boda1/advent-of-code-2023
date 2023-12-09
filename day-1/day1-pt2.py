with open('./input.txt') as f:
    numbers = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    calibration_sum = 0
    for line in f.read().split('\n'):
        for char in line:
            if char.isnumeric():
                if any(number in line.split(char, 1)[0] for number in numbers):
                    all_matches = sorted({line.find(number): number for number in numbers if number in line}.items())
                    x_index_word = all_matches[0][0]

                    if line.index(char) < x_index_word:
                        x = char
                    else:
                        x = numbers.index(all_matches[0][1]) + 1
                else:
                    x = char
                if any(number in line.split(char, 1)[1] for number in numbers):
                    all_matches = sorted({line.rfind(number): number for number in numbers if number in line}.items())
                    y_index_of_last_word = all_matches[len(all_matches) - 1][0]
                    y_index_of_last_number = 0

                    for i in range(len(line) - 1, -1, -1):
                        if line[i].isnumeric():
                            y_index_of_last_number = i
                            break

                    if y_index_of_last_word > y_index_of_last_number:
                        y = numbers.index(all_matches[len(all_matches) - 1][1]) + 1
                    else:
                        y = line[y_index_of_last_number]
                else:
                    for i in range(len(line) - 1, -1, -1):
                        if line[i].isnumeric():
                            y = line[i]
                            break
                break
        calibration_sum += int(str(x) + str(y))
        print(calibration_sum)
