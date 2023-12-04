

# I SUCKED AT THIS ONE lol
def findEnginePart():
    with open('./day3/input.txt') as f:
        matrix = f.readlines()
        gears = dict()
        sum = 0

        for line_id, line in enumerate(matrix):
            # clean lines
            matrix[line_id] = line.strip()

            nr = ''
            is_correct = False

            #look for gears
            for char_id, char in enumerate(line):
                if char == '*':
                    gears[(line_id, char_id)] = []

            # parse lines char by char
            for char_id, char in enumerate(line):

                if char.isdigit():
                    nr+=char

                    # Check if next to symbol
                    if line_id == 0:
                        top_left = False
                        top_right = False
                        top = False
                        bot = matrix[line_id + 1][char_id] != '.' and not matrix[line_id + 1][char_id].isdigit()

                        if char_id == 0:
                            left = False
                            bot_left = False
                        else:
                            left = matrix[line_id][char_id - 1] != '.'  and not matrix[line_id][char_id - 1].isdigit()
                            bot_left = matrix[line_id + 1][char_id - 1] != '.' and not matrix[line_id + 1][char_id - 1].isdigit()

                        if char_id < len(line) - 1:
                            right = matrix[line_id][char_id + 1] != '.' and not matrix[line_id][char_id + 1].isdigit()
                            bot_right = matrix[line_id + 1][char_id + 1] != '.' and not matrix[line_id + 1][char_id + 1].isdigit()
                        else:
                            right = False
                            bot_right = False

                    elif line_id == len(matrix) - 1:
                        bot_left = False
                        bot_right = False
                        bot = False
                        top = matrix[line_id - 1][char_id] != '.' and not matrix[line_id - 1][char_id].isdigit()

                        if char_id == 0:
                            left = False
                            top_left = False
                        else:
                            left = matrix[line_id][char_id - 1] != '.'  and not matrix[line_id][char_id - 1].isdigit()
                            top_left = matrix[line_id - 1][char_id - 1] != '.' and not matrix[line_id - 1][char_id - 1].isdigit()

                        if char_id < len(line) - 1:
                            right = matrix[line_id][char_id + 1] != '.' and not matrix[line_id][char_id + 1].isdigit()
                            top_right = matrix[line_id - 1][char_id + 1] != '.' and not matrix[line_id - 1][char_id + 1].isdigit()
                        else:
                            right = False
                            top_right = False 
                    else:
                        bot = matrix[line_id + 1][char_id] != '.' and not matrix[line_id + 1][char_id].isdigit()
                        top = matrix[line_id - 1][char_id] != '.' and not matrix[line_id - 1][char_id].isdigit()

                        if char_id == 0:
                            left = False
                            top_left = False
                            bot_left = False
                        else:
                            left = matrix[line_id][char_id - 1] != '.'  and not matrix[line_id][char_id - 1].isdigit()
                            top_left = matrix[line_id - 1][char_id - 1] != '.' and not matrix[line_id - 1][char_id - 1].isdigit()
                            bot_left = matrix[line_id + 1][char_id - 1] != '.' and not matrix[line_id + 1][char_id - 1].isdigit()

                        if char_id < len(line) - 2:
                            right = matrix[line_id][char_id + 1] != '.' and not matrix[line_id][char_id + 1].isdigit()
                            top_right = matrix[line_id - 1][char_id + 1] != '.' and not matrix[line_id - 1][char_id + 1].isdigit()
                            bot_right = matrix[line_id + 1][char_id + 1] != '.' and not matrix[line_id + 1][char_id + 1].isdigit()
                        else:
                            right = False
                            top_right = False 
                            bot_right = False

                    if left or right or top or bot or bot_left or bot_right or top_left or top_right:
                        is_correct = True

                    # left
                    if matrix[line_id][char_id - 1] == "*":
                        (line_id, char_id)
                    right = matrix[line_id][char_id - 1] == "*"
                    top = matrix[line_id][char_id - 1] == "*"
                    bot = matrix[line_id][char_id - 1] == "*"

                    
                else:
                    if is_correct:
                        sum += int(nr)

                    # reset NR
                    is_correct = False
                    nr = ''

        return sum

def getGearRatio():
    with open('./day3/out.txt') as f:
        matrix = f.readlines()
        gears = dict()

        #look for gears
        for line_id, line in enumerate(matrix):
            for char_id, char in enumerate(line):
                if char == '*':
                    gears[(line_id, char_id)] = []

        nr = ''
        to_check = []

        #look for numbers
        for line_id, line in enumerate(matrix):
            for char_id, char in enumerate(line):
                
                if char.isdigit():
                    nr += char

                    if not line[char_id - 1].isdigit() and not line[char_id + 1].isdigit():
                        #top
                        to_check.append((line_id - 1, char_id))
                        #top_left
                        to_check.append((line_id - 1, char_id - 1))
                        #left
                        to_check.append((line_id, char_id - 1))
                        #bot_left
                        to_check.append((line_id + 1, char_id - 1))
                        #bot
                        to_check.append((line_id + 1, char_id))
                        #top_right
                        to_check.append((line_id - 1, char_id + 1))
                        #right
                        to_check.append((line_id, char_id + 1))
                        #bot_right
                        to_check.append((line_id + 1, char_id + 1))

                    elif not line[char_id - 1].isdigit():
                        #top
                        to_check.append((line_id - 1, char_id))
                        #top_left
                        to_check.append((line_id - 1, char_id - 1))
                        #left
                        to_check.append((line_id, char_id - 1))
                        #bot_left
                        to_check.append((line_id + 1, char_id - 1))
                        #bot
                        to_check.append((line_id + 1, char_id))

                    elif line[char_id - 1].isdigit() and line[char_id + 1].isdigit():
                        #top
                        to_check.append((line_id - 1, char_id))
                        #bot
                        to_check.append((line_id + 1, char_id))
                        
                    elif not line[char_id + 1].isdigit():
                        #top
                        to_check.append((line_id - 1, char_id))
                        #top_right
                        to_check.append((line_id - 1, char_id + 1))
                        #right
                        to_check.append((line_id, char_id + 1))
                        #bot_right
                        to_check.append((line_id + 1, char_id + 1))
                        #bot
                        to_check.append((line_id + 1, char_id))

                else:
                    for coords in to_check:
                        if coords in gears.keys():
                            gears[coords].append(nr)

                    to_check = []
                    nr = ''
        
    sum = 0

    for numbers in gears.values():
        if len(numbers) == 2:
            print(numbers)
            ratio = 1
            for i in numbers:
                ratio *= int(i)

            sum += ratio

    return sum
                           
def addPadding():
    output = open('./puzzle3/out.txt', 'w')

    with open('./puzzle3/input.txt', 'r') as inp:
        matrix = inp.readlines()

        for line_id, line in enumerate(matrix):
            # clean lines
            # line = line.strip()
            new_line = '.'
            new_line += line.strip()
            new_line += '.\n'

            output.write(new_line)

            # print(len(new_line))

    output.close()

if __name__ == "__main__":
    print(getGearRatio())
    # addPadding()