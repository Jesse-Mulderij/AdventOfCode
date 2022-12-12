def num_of_fully_contained_elves(t):
    f = open(t)
    lines = f.readlines()
    num_of_pairs = 0
    for line in lines:
        ranges = line.strip().split(",")
        range_elf = []
        taskset = [set(), set()]
        for ran in ranges:
            range_elf.append(ran.split("-"))
        for ii, bound in enumerate(range_elf):
            tasklist = list(range(int(bound[0]), int(bound[1]) + 1))
            for task in tasklist:
                taskset[ii].add(task)
        if (
            taskset[0].union(taskset[1]) == taskset[0]
            or taskset[0].union(taskset[1]) == taskset[1]
        ):
            num_of_pairs += 1
    f.close()
    return num_of_pairs


def num_of_overlapping_elves(t):
    f = open(t)
    lines = f.readlines()
    num_of_pairs = 0
    for line in lines:
        ranges = line.strip().split(",")
        range_elf = []
        taskset = [set(), set()]
        for ran in ranges:
            range_elf.append(ran.split("-"))
        for ii, bound in enumerate(range_elf):
            tasklist = list(range(int(bound[0]), int(bound[1]) + 1))
            for task in tasklist:
                taskset[ii].add(task)
        if not taskset[0].isdisjoint(taskset[1]):
            num_of_pairs += 1
    f.close()
    return num_of_pairs


def main():
    x = num_of_fully_contained_elves("Day 4/testinput.txt")
    print(x)
    x = num_of_fully_contained_elves("Day 4\input.txt")
    print(x)
    x = num_of_overlapping_elves("Day 4\input.txt")
    print(x)


if __name__ == "__main__":
    main()
