import math
from functools import reduce

# helpers


def readData(path):
    with open(path, 'r') as file:
        lines = file.readlines()

        # separate lines
        instructions = lines[0].strip()
        world_map = [l.strip().split(' = ') for l in lines[2::]]

    return (world_map, instructions)


def traverse_map(map_dict, instructions, current_position, total_steps=0):
    has_arrived = False

    for step in instructions:
        match step:
            case 'L':
                current_position = map_dict[current_position][0]
                total_steps += 1
            case 'R':
                current_position = map_dict[current_position][1]
                total_steps += 1

        if current_position == 'ZZZ':
            has_arrived = True
            break

    return has_arrived, total_steps, current_position

# Part 1


def solve(world_map, instructions):
    # clean world_map input
    world_map = [[l[0], l[1].replace('(', '').replace(
        ')', '').split(', ')] for l in world_map]

    # map values to dict
    map_dict = dict()
    for element in world_map:
        map_dict[element[0]] = (element[1][0], element[1][1])

    # solve map
    current_position = 'AAA'
    status, total_steps, current_position = traverse_map(
        map_dict, instructions, current_position)

    while not status:
        status, total_steps, current_position = traverse_map(
            map_dict, instructions, current_position, total_steps)

    return total_steps


# Part 2
# a bit convoluted but it works

def iterateInstructions(map_dict, instructions, current_pos, total_steps):
    status = False

    new_pos = current_pos
    for i in instructions:
        match i:
            case 'L':
                new_pos = map_dict[new_pos][0]
            case 'R':
                new_pos = map_dict[new_pos][1]

        total_steps += 1

        if new_pos[-1] == 'Z':
            status = True
            break

    return status, total_steps, new_pos


def traverse_ghost_map(map_dict, instructions, start_pos):
    counting = []

    for step in start_pos:
        curr_step = step
        currentTotal = 0
        status, currentTotal, curr_step = iterateInstructions(
            map_dict, instructions, curr_step, currentTotal)

        while not status:
            status, currentTotal, curr_step = iterateInstructions(
                map_dict, instructions, curr_step, currentTotal)

        counting.append(currentTotal)

    total = 1

    for i in counting:
        total = total * i // math.gcd(total, i)

    return total


def ghostSolve(world_map, instructions):
    # clean world_map input
    world_map = [[l[0], l[1].replace('(', '').replace(
        ')', '').split(', ')] for l in world_map]
    # map values to dict
    map_dict = dict()
    for element in world_map:
        map_dict[element[0]] = (element[1][0], element[1][1])

    # solve map
    current_positions = [key for key in map_dict.keys() if key[-1] == 'A']
    total_steps = traverse_ghost_map(map_dict, instructions, current_positions)

    return total_steps


if __name__ == '__main__':
    world_map, instructions = readData('./input/day8.txt')
    result = ghostSolve(world_map, instructions)
    print(result)
