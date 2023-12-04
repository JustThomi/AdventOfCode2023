numbers = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

def getCalibration():
    with open('./day1/input.txt', 'r') as f:
        lines = f.readlines()
        sum = 0

        for line in lines:
            nr = None
            sub_string = ''

            for letter in line:
                sub_string += letter

                for word in numbers:
                    if word in sub_string:
                        nr = str(numbers.index(word))
                        break

                if not nr:
                    if letter.isdigit():
                        nr = letter
                        break
                else:
                    break
            
            rev_line = line[::-1]
            sub_string = ''
            first_nr = nr

            for letter in rev_line:
                sub_string = letter + sub_string

                for word in numbers:
                    if word in sub_string:
                        nr += str(numbers.index(word))
                        break

                if nr == first_nr:
                    if letter.isdigit():
                        nr += letter
                        break
                else:
                    break

            sum += int(nr)

    return sum

if __name__ == "__main__":
    print(getCalibration())