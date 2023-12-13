import re


def findWinnings():
    with open('./puzzle4/input.txt') as f:
        lines = f.readlines()
        sum = 0

        for line_id, line in enumerate(lines):
            # clean lines
            spaceless = re.sub(r'\s+', ' ', line)
            clean_lines = spaceless.split(
                'Card ' + str(line_id + 1) + ': ')[1].strip()
            separate_lines = clean_lines.split('|')

            # separate winning numbers and your numbers
            winning_numbers = [int(i)
                               for i in separate_lines[0].split(' ') if i != '']
            your_numbers = [int(i)
                            for i in separate_lines[1].split(' ') if i != '']

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


def storeCards():
    with open('./inputs/day4.txt') as f:
        lines = f.readlines()
        cards = dict()

        # separate cards
        for line_id, line in enumerate(lines):
            # clean lines
            spaceless = re.sub(r'\s+', ' ', line)
            clean_lines = spaceless.split(
                'Card ' + str(line_id + 1) + ': ')[1].strip()
            separate_lines = clean_lines.split('|')

            # separate winning numbers and your numbers
            winning_numbers = [int(i)
                               for i in separate_lines[0].split(' ') if i != '']
            your_numbers = [int(i)
                            for i in separate_lines[1].split(' ') if i != '']

            # check total numbers
            total_matches = 0
            for nr in your_numbers:
                if nr in winning_numbers:
                    total_matches += 1

            # create dict
            cards[line_id + 1] = [winning_numbers, your_numbers, total_matches]

    return cards


def countCards(cards, copies, s):
    copy = []
    final_sum = s

    for item in copies:
        total = item[1]

        if total > 0:
            for i in range(1, total + 1):
                if item[0] + i in cards.keys():
                    copy.append([item[0] + i, cards[item[0] + i][2]])

    final_sum += len(copy)

    if len(copy) > 0:
        final_sum = countCards(cards, copy, final_sum)

    return final_sum


if __name__ == "__main__":
    cards = storeCards()
    list_cards = [[key, value[2]] for key, value in cards.items()]

    sum = len(cards.keys())

    print(countCards(cards, list_cards, sum))
