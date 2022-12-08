def calculate_score_per_round(enemy, you):
    loss_draw_win = [0, 3, 6]
    keys = ["A",'B',"C","X","Y","Z"]
    values = [1,2,3,1,2,3]
    dicts = {}
    for i in range(len(keys)):
        dicts[keys[i]] = values[i]
    return loss_draw_win[(-dicts[enemy] + dicts[you] + 1) % 3] + dicts[you]

def calculate_score(t):
    f = open(t)
    lines = f.readlines()
    sum = 0
    for line in lines:
        sum += calculate_score_per_round(line[0],line[2])
    f.close()
    return sum

def main():
    x = calculate_score("input.txt")
    print(x)

main()