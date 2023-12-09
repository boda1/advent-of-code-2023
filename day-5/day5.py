with open('./input.txt') as f:
    for block in f.read().split('\n\n'):
        if block.startswith('seeds'):
            seed_numbers = [int(seed_number) for seed_number in block.split(' ') if seed_number.isnumeric()]

        for line in block.split('\n'):
            if line[0].isalpha():
                mapped = [False] * len(seed_numbers)
                print(f"{line} - setting mapped statuses to false")
            if line[0].isnumeric():
                mappings = [int(i) for i in line.split(' ')]
                destination_start, source_start, steps = mappings

                for index, seed in enumerate(seed_numbers):
                    x = seed - source_start
                    y = seed - (source_start + steps)
                    if y <= 0 <= x:
                        if mapped[index] is False:
                            new_seed_value = destination_start + x
                            seed_numbers[index] = new_seed_value
                        mapped[index] = True
                    else:
                        pass

        print(sorted(seed_numbers))