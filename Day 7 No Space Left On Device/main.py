import directory, file


def parse_input(lines):

    home = directory.directory("/", None, [], [])
    current_dir = home
    for line in lines[1:]:
        splitline = line.strip().split(" ")
        if line[0] == "$":
            if line[2:4] == "cd":
                if line[5] == "/":
                    current_dir = home
                elif line[5:7] == "..":
                    current_dir = current_dir.parent
                else:
                    name = line[5:].strip()
                    for dir in current_dir.dirlist:
                        if dir.name == name:
                            current_dir = dir
            elif line[2:4] == "ls":
                continue
            else:
                raise AssertionError("Unknown command")

        # check if we are exploring a dir
        elif splitline[0] == "dir":
            # check if current dir already contains a dir with this name
            name = splitline[1]
            contains_dir = False
            for dir in current_dir.dirlist:
                if dir.name == name:
                    contains_dir = True

            # if not, add the newly explored dir to the current dir's dirlist
            if not contains_dir:
                current_dir.add_dir(
                    directory.directory(name, current_dir, [], [])
                )

        # then we must be exploring a file
        else:
            # check if current dir already contains a file with this name
            name = splitline[1]
            contains_file = False
            for f in current_dir.filelist:
                if f.name == name:
                    contains_file = True

            # if not, add the newly explored dir to the current dir's dirlist
            if not contains_file:
                current_dir.add_file(file.file(name, int(splitline[0])))

    return home


def size_sum_of_small_dirs(t) -> int:
    f = open(t)
    lines = f.readlines()

    home = parse_input(lines)
    small_dir_list = []
    sum = 0

    for dir in home.get_all_subdirs():
        if dir.get_size() <= 100000:
            # small_dir_list.append(dir)
            sum += dir.get_size()

    return sum


def size_of_smallest_large_enough_dir(t) -> int:
    f = open(t)
    lines = f.readlines()
    total_space = 70000000
    req_unused_space = 30000000
    home = parse_input(lines)
    min_space_to_free = home.get_size() - total_space + req_unused_space
    if min_space_to_free <= 0:
        return 0
    else:
        dir_to_remove = home
        for dir in home.get_all_subdirs():
            dir_size = dir.get_size()
            if (
                dir_size > min_space_to_free
                and dir_size < dir_to_remove.get_size()
            ):
                dir_to_remove = dir
        return dir_to_remove.get_size()


def main():
    test = "Day 7 No Space Left On Device/testinput.txt"
    real = "Day 7 No Space Left On Device\input.txt"

    x = size_sum_of_small_dirs(test)
    print(x)
    x = size_sum_of_small_dirs(real)
    print(x)

    x = size_of_smallest_large_enough_dir(test)
    print(x)
    x = size_of_smallest_large_enough_dir(real)
    print(x)


if __name__ == "__main__":
    main()
