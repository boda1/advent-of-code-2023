with open('./input.txt') as f:
    for block in f.read().split('\n\n'):
        if block.startswith('seeds'):
            all_seeds = block.split(' ')
            seed_numbers_list = [int(seed_number) for seed_number in all_seeds if seed_number.isnumeric()]
            seed_number_ranges = {}
            seed_numbers = {}

            for idx in range(0, len(seed_numbers_list), 2):
                seed_numbers_start = seed_numbers_list[idx]
                seed_numbers_end = seed_numbers_list[idx] + (seed_numbers_list[idx + 1] - 1)
                seed_number_ranges[idx] = [seed_numbers_start, seed_numbers_end]

        for line in block.split('\n'):
            if line[0].isalpha():
                print(line)
                mapped = [False]
                for index, mapped_status in seed_numbers.items():
                    mapped_status[0] = False

            if line[0].isnumeric():
                mappings = [int(i) for i in line.split(' ')]
                destination_start, source_start, steps = mappings

                for seed_start, seed_end in seed_number_ranges.values():
                    print(seed_start, seed_end)
                    for index, seed in enumerate(range(seed_start, seed_end)):
                        seed_numbers[index] = [False, seed]
                        x = seed - source_start
                        y = seed - (source_start + steps)
                        if y <= 0 <= x:
                            if seed_numbers[index][0] is False:
                                new_seed_value = destination_start + x
                                seed_numbers[index][1] = new_seed_value
                            seed_numbers[index][0] = True
                        else:
                            pass
                    print(seed_numbers)
            # print(sorted(seed_numbers.values()))
