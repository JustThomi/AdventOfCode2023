
# WORSE solution EUNE :))

# PART 1
def mapValues():
    with open('./day5/test.txt') as f:
        lines = f.readlines()
        # categories = ['seed_soile', 'soile_fertilizer', 'fertilizer_water', 'water_light', 'light_temp', 'temp_humidity', 'humidity_location']
        ranges = []
        seeds = []
        # get seeds
        seeds = lines[0].split('seeds: ')[1].strip().split(' ')
        seeds = [int(i) for i in seeds]

        # clean lines
        lines= lines[3:]
        line_iter = iter(lines)
        
        # convenient stuff
        next_category = '\n'

        # save ranges
        for line in line_iter:
            # next category, reset dict
            if line == next_category:
                final_seeds = []

                for seed in seeds:
                    val = seed
                    for r in ranges:
                        destination_range = r[0]
                        source_range = r[1]
                        range_val = r[2]

                        if seed >= source_range and seed <= source_range + range_val:
                            val = destination_range + (seed - source_range)
                            break
                    
                    final_seeds.append(val)
                            
                seeds = final_seeds
                ranges = []
                next(line_iter)
                continue

            numbers = line.strip().split(' ')
            numbers = [int(i) for i in numbers]
            ranges.append(numbers)

    return min(seeds)



# PART 2

def load_file():
    with open('./day5/input.txt') as f:
        lines = f.readlines()
        ranges = []

        # get seeds
        seed_range = lines[0].split('seeds: ')[1].strip().split(' ')
        seed_range = [int(i) for i in seed_range]

        # clean lines
        lines= lines[3:]

    return seed_range, lines

def seedButRange(seed_range, line_iter):        
    min_location = None

    for sr in range(0, len(seed_range), 2):
        print('Started range', sr)
        seed_start = seed_range[sr]
        seed_end = seed_start + seed_range[sr + 1]

        for seed in range(seed_start, seed_end + 1):
            translation = translate_seed(seed, line_iter)

            if min_location == None or translation < min_location:
                min_location = translation

        print('ended range', sr)
    return min_location


def translate_seed(seed, lines):
    # convenient stuff
    next_category = '\n'
    val = seed
    ranges = []
    line_iter = iter(lines)


    for line in line_iter:
        # next category, reset dict
        if line == next_category:
            for r in ranges:
                destination_range = r[0]
                source_range = r[1]
                range_val = r[2]

                if val >= source_range and val <= source_range + range_val:
                    val = destination_range + (val - source_range)
                    break

            ranges = []
            next(line_iter)
            continue

        numbers = line.strip().split(' ')
        numbers = [int(i) for i in numbers]
        ranges.append(numbers)

    return val

if __name__ == "__main__":
    seed_range, line_iter = load_file()
    print(seedButRange(seed_range, line_iter))
