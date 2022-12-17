from typing import List

def parse_input(t : str) -> List[list]:
    f = open(t)
    lines = f.readlines()

    forest = []
    y = -1
    for line in lines:
        x = 0
        y += 1
        forest.append([])
        for h in line.strip():
            forest[y].append(h)
    return forest

def is_visible_from_right(forest: List[list], tree: List[int]) -> bool:
    is_visible_from_right = True
    for x in range(tree[0] + 1, len(forest[0])):
        if forest[tree[0]][tree[1]] <= forest[x][tree[1]]:
            is_visible_from_right = False
    return is_visible_from_right


def is_visible_from_top(forest: List[list], tree: List[int]) -> bool:
    is_visible_from_top = True
    for y in range(0, tree[1]):
        if forest[tree[0]][tree[1]] <= forest[tree[0]][y]:
            is_visible_from_top = False
    return is_visible_from_top


def is_visible_from_left(forest: List[list], tree: List[int]) -> bool:
    is_visible_from_left = True
    for x in range(0, tree[0]):
        if forest[tree[0]][tree[1]] <= forest[x][tree[1]]:
            is_visible_from_left = False
    return is_visible_from_left


def is_visible_from_bottom(forest: List[list], tree: List[int]) -> bool:
    is_visible_from_bottom = True
    for y in range(tree[1] + 1, len(forest[0])):
        if forest[tree[0]][tree[1]] <= forest[tree[0]][y]:
            is_visible_from_bottom = False
    return is_visible_from_bottom


def is_visible(forest: List[list], tree: List[int]) -> bool:
    # if tree is on the edge, it is visible
    if tree[0] == len(forest) or tree[1] == len(forest[0]):
        return True

    # tree is not on the bottom/right edge (that is when edge cases occur)
    else:
        return (
            is_visible_from_right(forest, tree)
            or is_visible_from_top(forest, tree)
            or is_visible_from_left(forest, tree)
            or is_visible_from_bottom(forest, tree)
        )

def visual_range_to_right(forest : List[list], tree : List[int]) -> int:
    visual_range = 1
    for x in range(tree[0] + 1, len(forest[0])-1):
        if forest[tree[0]][tree[1]] > forest[x][tree[1]]:
            visual_range += 1
        else:
            return visual_range
    return visual_range

def visual_range_to_top(forest: List[list], tree: List[int]) -> bool:
    visual_range = 1
    yrange = list(range(1, tree[1]))
    yrange.reverse()
    for y in yrange:
        if forest[tree[0]][tree[1]] > forest[tree[0]][y]:
            visual_range += 1
        else:
            return visual_range
    return visual_range

def visual_range_to_left(forest: List[list], tree: List[int]) -> bool:
    visual_range = 1
    xrange = list(range(1, tree[0]))
    xrange.reverse()
    for x in xrange:
        if forest[tree[0]][tree[1]] > forest[x][tree[1]]:
            visual_range += 1
        else:
            return visual_range
    return visual_range

def visual_range_to_bottom(forest: List[list], tree: List[int]) -> bool:
    visual_range = 1
    for y in range(tree[1] + 1, len(forest[0])-1):
        if forest[tree[0]][tree[1]] > forest[tree[0]][y]:
            visual_range += 1
        else:
            return visual_range
    return visual_range

def scenic_score(forest : List[list], tree : List[list]) -> int:
    ymax = len(forest)
    xmax = len(forest[0])
    if tree[0] == 0 or tree[0] == xmax-1 or tree[1] == 0 or tree[1] == ymax-1:
        return 0
    else:
        scenic_score = visual_range_to_right(forest, tree) * visual_range_to_top(forest, tree) * visual_range_to_left(forest, tree) * visual_range_to_bottom(forest, tree)
        return scenic_score

def count_visible_trees(t: str) -> int:
    forest = parse_input(t)

    num_of_visible_trees = 0
    ymax = len(forest)
    xmax = len(forest[0])
    for x in range(xmax):
        for y in range(ymax):
            tree = [x, y]
            if is_visible(forest, tree):
                num_of_visible_trees += 1

    return num_of_visible_trees

def calc_scenic_score(t : str) -> int:
    forest = parse_input(t)
    max_score = 0
    ymax = len(forest)
    xmax = len(forest[0])
    for x in range(xmax):
        for y in range(ymax):
            tree = [x,y]
            current_score = scenic_score(forest, tree)
            if max_score < current_score:
                max_score = current_score
                print([x,y])
    return max_score
    

def main():
    test = "Day 8 Treetop Tree House/testinput.txt"
    real = "Day 8 Treetop Tree House\input.txt"

    x = count_visible_trees(test)
    print(x)
    x = count_visible_trees(real)
    print(x)

    x = calc_scenic_score(test)
    print(x)
    x = calc_scenic_score(real)
    print(x)


if __name__ == "__main__":
    main()
