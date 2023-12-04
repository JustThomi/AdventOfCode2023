import re

def findWinnings():
    with open('./puzzle4/input.txt') as f:
        lines = f.readlines()
        sum = 0

        for line_id, line in enumerate(lines):
            # clean lines
            spaceless = re.sub(r'\s+', ' ', line)
            clean_lines = spaceless.split('Card ' + str(line_id + 1) + ': ')[1].strip()
            separate_lines = clean_lines.split('|')

            # separate winning numbers and your numbers
            winning_numbers = [int(i) for i in separate_lines[0].split(' ') if i != '']
            your_numbers = [int(i) for i in separate_lines[1].split(' ') if i != '']

            total_matches = 0
            # check total numbers
            for nr in your_numbers:
                if nr in winning_numbers:
                    if total_matches == 0:
                        total_matches = 1
                    else:
                        total_matches *= 2
            
            sum += total_matches
    
    return sum

def totalCards():
    with open('./day4/input.txt') as f:
        lines = f.readlines()
        cards = dict()
        copy_cards = dict()
        sum = 0

        # separate cards
        for line_id, line in enumerate(lines):
            # clean lines
            spaceless = re.sub(r'\s+', ' ', line)
            clean_lines = spaceless.split('Card ' + str(line_id + 1) + ': ')[1].strip()
            separate_lines = clean_lines.split('|')

            # separate winning numbers and your numbers
            winning_numbers = [int(i) for i in separate_lines[0].split(' ') if i != '']
            your_numbers = [int(i) for i in separate_lines[1].split(' ') if i != '']
            
            # check total numbers
            total_matches = 0
            for nr in your_numbers:
                if nr in winning_numbers:
                    total_matches += 1
            
            # create dict
            cards[line_id] = [winning_numbers, your_numbers, total_matches]
            
        
        # count copies
        for key, value in cards.items():
            print(key, value)
        
    
    return sum


def countCards(cards, copy, sum):
    pass

if __name__ == "__main__":
    print(totalCards())