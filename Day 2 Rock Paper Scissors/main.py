def calculate_score_per_round(enemy, you):
    loss_draw_win = [0, 3, 6]
    keys = ["A", "B", "C", "X", "Y", "Z"]
    values = [1, 2, 3, 1, 2, 3]
    dicts = {}
    for i in range(len(keys)):
        dicts[keys[i]] = values[i]
    return loss_draw_win[(-dicts[enemy] + dicts[you] + 1) % 3] + dicts[you]


def calculate_alternative_score_per_round(enemy, you):
    outcome_dict = {}
    keys = ["X", "Y", "Z"]
    values = [0, 3, 6]
    for i in range(len(keys)):
        outcome_dict[keys[i]] = values[i]

    outcome = outcome_dict[you]

    keys = ["A", "B", "C", "X", "Y", "Z"]
    values = [0, 1, 2, -1, 0, 1]
    dicts = {}
    for i in range(len(keys)):
        dicts[keys[i]] = values[i]
    your_choice = 1 + ((dicts[enemy] + dicts[you]) % 3)

    return outcome + your_choice


def calculate_score(t):
    f = open(t)
    lines = f.readlines()
    sum = 0
    for line in lines:
        sum += calculate_score_per_round(line[0], line[2])
    f.close()
    return sum


def calculate_alternative_score(t):
    f = open(t)
    lines = f.readlines()
    sum = 0
    for line in lines:
        sum += calculate_alternative_score_per_round(line[0], line[2])
    f.close()
    return sum


def main():
    x = calculate_score("Day 2 Rock Paper Scissors\input.txt")
    print(x)
    x = calculate_alternative_score("Day 2 Rock Paper Scissors\input.txt")
    print(x)


main()
