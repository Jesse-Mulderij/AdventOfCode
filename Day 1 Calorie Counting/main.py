def find_most_calories(t):

    f = open(t)
    lines = f.readlines()
    highest_cals = 0
    current_cals = 0

    for line in lines:
        if line == "\n":
            if current_cals > highest_cals:
                highest_cals = current_cals
            current_cals = 0
        else:
            current_cals += int(line)

    f.close()
    return highest_cals


def find_3_most_calories(t):

    f = open(t)
    lines = f.readlines()
    three_highest_cals = [0, 0, 0]
    current_cals = 0

    for line in lines:
        if line == "\n":
            if current_cals > three_highest_cals[0]:
                three_highest_cals[0] = current_cals
                three_highest_cals.sort()

            current_cals = 0
        else:
            current_cals += int(line)

    f.close()
    sum = 0
    for ii in three_highest_cals:
        sum += ii
    return sum


def main():
    x = find_most_calories("Day 1 Calorie Counting\input.txt")
    print(x)

    x = find_3_most_calories("Day 1 Calorie Counting\input.txt")
    print(x)


main()
