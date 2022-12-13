from typing import List


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


def count_visible_trees(t: str):
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

    num_of_visible_trees = 0
    ymax = len(forest)
    xmax = len(forest[0])
    for x in range(xmax):
        for y in range(ymax):
            tree = [x, y]
            if is_visible(forest, tree):
                num_of_visible_trees += 1

    return num_of_visible_trees


def main():
    test = "Day 8 Treetop Tree House/testinput.txt"
    real = "Day 8 Treetop Tree House\input.txt"

    x = count_visible_trees(test)
    print(x)
    x = count_visible_trees(real)
    print(x)

    x = count_visible_trees(test)
    print(x)
    x = count_visible_trees(real)
    print(x)


if __name__ == "__main__":
    main()
