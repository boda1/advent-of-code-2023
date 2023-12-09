import math


def calculate_number_of_winning_rounds(time_and_distance):
    wins = 0
    race_time = int(time_and_distance[0])
    race_record = int(time_and_distance[1])
    print(race_time, race_record)

    for second in range(race_time):
        if second * (race_time - second) > race_record:
            wins += 1

    return wins


with open('./input.txt') as f:
    total_wins = []

    for line in f.read().split('\n'):
        if line.startswith('Time'):
            time = [value for value in line.split(' ') if value.isnumeric()]
        if line.startswith('Distance'):
            distance = [value for value in line.split(' ') if value.isnumeric()]

    past_race_time_and_distance = set(zip(time, distance))

    for item in past_race_time_and_distance:
        total_wins.append(calculate_number_of_winning_rounds(item))

    print(math.prod(total_wins))
