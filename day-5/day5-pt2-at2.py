def get_seeds(block):
    seed_numbers_list = [int(seed_number) for seed_number in block.split(' ') if seed_number.isnumeric()]
    seed_number_ranges = {}

    for idx in range(0, len(seed_numbers_list), 2):
        seed_numbers_start = seed_numbers_list[idx]
        seed_numbers_end = seed_numbers_list[idx] + (seed_numbers_list[idx + 1] - 1)
        seed_number_ranges[idx] = [seed_numbers_start, seed_numbers_end]

    return seed_number_ranges


with open('./input.txt') as f:
    all_mapping_blocks = []

    for block in f.read().split('\n\n'):
        if block.startswith('seeds'):
            seed_number_ranges = get_seeds(block)
        else:
            all_mapping_blocks.append(block)

    print(seed_number_ranges)
    print(all_mapping_blocks)




    """

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
        """