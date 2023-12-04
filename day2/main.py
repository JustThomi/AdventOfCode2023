input_balls = {
    'red' : 12,
    'blue' : 14,
    'green': 13,
}

def realGame():
    with open('./day2/input.txt', 'r') as file:
        lines = file.readlines()
        sum = 0

        for line in lines:
            results = dict()

            game_id = lines.index(line) + 1
            gameless_line = line.split('Game ' + str(game_id) + ': ')[1]

            reveal_list = gameless_line.split('; ')

            for reveal in reveal_list:
                cubes = reveal.split(', ')

                for cube in cubes:
                    counting = cube.split(' ')
                    counting[1] = counting[1].strip()

                    if counting[1] not in results.keys():
                        results[counting[1]] = int(counting[0])
                    elif results[counting[1]] < int(counting[0]):
                        results[counting[1]] = int(counting[0])

            power = 1
            for key, value in results.items():
                power *= value
            
            sum += power
    
    return sum


if __name__ == "__main__":
    print(realGame())



# FOR PART ONE
# is_real = True
# for key, value in results.items():
#     if value > input_balls[key]:
#         is_real = False
#
# if is_real:
#     sum += game_id