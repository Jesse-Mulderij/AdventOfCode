import re
from typing import List

def parse_stack_input(lines : List[str]) -> List[list]:
    at_move_input = False
    num_of_stacks = int(len(lines[0])/4)
    stacks = list()
    for ii in range(num_of_stacks):
        stacks.append(list())

    for line in lines:
        if at_move_input:
            for stack in stacks:
                stack.reverse()
            return stacks
        elif line.strip()[0] != "[":
            at_move_input = True
        else:
            for ii in range(num_of_stacks):
                char = line[4*ii + 1]
                if char != ' ':
                    stacks[ii].append(char)
    raise AssertionError("Should have returned before ending for loop")


def parse_move_input(lines : List[str]) -> List[list]:
    moves = list()
    at_move_input = False
    for line in lines:
        if at_move_input:
            move = [eval(i) for i in re.findall('[0-9]+', line)]
            move[1] -= 1
            move[2] -= 1
            moves.append(move)
        else:
            if line == "\n":
                at_move_input = True
    return moves


def process_move_n_from_a_to_b_9000(stacks : List[list], n : int, a : int, b : int) -> None:
    for ii in range(n):
        stacks[b].append(stacks[a].pop())

def process_move_n_from_a_to_b_9001(stacks : List[list], n : int, a : int, b : int) -> None:
    stack_to_move = []
    for ii in range(n):
        stack_to_move.insert(0, stacks[a].pop())
    stacks[b] += stack_to_move

def crates_on_top_of_stacks(t : str, crane_type : int) -> str:
    f = open(t)
    lines = f.readlines()
    stacks = parse_stack_input(lines)
    moves = parse_move_input(lines)

    for move in moves:
        [n, a, b] = move
        if crane_type == 9000:
            process_move_n_from_a_to_b_9000(stacks, n, a, b)
        elif crane_type == 9001:
            process_move_n_from_a_to_b_9001(stacks, n, a, b)
        else:
            raise AssertionError("Unknown crane type")

    crates_on_top = ''
    for stack in stacks:
        crates_on_top += (stack[len(stack)-1])

    return crates_on_top



def main():
    x = crates_on_top_of_stacks("Day 5 Supply Stacks/testinput.txt", 9000)
    print(x)
    x = crates_on_top_of_stacks("Day 5 Supply Stacks\input.txt", 9000)
    print(x)
    x = crates_on_top_of_stacks("Day 5 Supply Stacks/testinput.txt", 9001)
    print(x)
    x = crates_on_top_of_stacks("Day 5 Supply Stacks\input.txt", 9001)
    print(x)


if __name__ == "__main__":
    main()
