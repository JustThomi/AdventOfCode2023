
def beatRecord():
    with open('./day6/input.txt', 'r') as file:
        lines = file.readlines()

        time = lines[0].strip().split('Time: ')[1].split()
        time = [int(i) for i in time]

        distance = lines[1].strip().split('Distance: ')[1].split()
        distance = [int(i) for i in distance]

        # get total tries
        total_wins = 1
        for idx in range(len(time)):
            current_time = time[idx]
            current_distance = distance[idx]

            count_winable = 0
            for hold_button in range(current_time):
                traveled = (current_time - hold_button) * hold_button

                if traveled > current_distance:
                    count_winable += 1

            total_wins *= count_winable

    return total_wins


def countWaysBigRace():
    with open('./inputs/day6.txt', 'r') as file:
        lines = file.readlines()

        # it can probs be done better
        times = lines[0].strip().split('Time: ')[1].split()
        time = ''
        for nr in times:
            time += nr
        time = int(time)

        distances = lines[1].strip().split('Distance: ')[1].split()
        distance = ''
        for nr in distances:
            distance += nr
        distance = int(distance)

        # count nr of winnable races

        count_winable = 0
        for hold_button in range(time):
            traveled = (time - hold_button) * hold_button

            if traveled > distance:
                count_winable += 1

    return count_winable


if __name__ == "__main__":
    print(countWaysBigRace())
