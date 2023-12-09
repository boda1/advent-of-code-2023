with open('./input.txt') as f:
    calibration_sum = 0
    for line in f.read().split('\n'):
        print(line)
        for char in line:
            if char.isnumeric():
                x = char
                break
        for i in range(len(line) - 1, -1, -1):
            if line[i].isnumeric():
                y = line[i]
                break
        num_to_add = x + y
        print(num_to_add)
        calibration_sum += int(num_to_add)
    print(calibration_sum)


