def unique(s : str) -> bool:
    s = list(s)
    s.sort()
    for ii in range(len(s) - 1):
        if s[ii] == s[ii+1]:
                return False
    return True

def chars_before_first_packet(t : str):
    f = open(t)
    line = f.readlines()[0]
    for ii in range(len(line)-3):
        s = line[ii:ii+4]
        if unique(s):
            return ii + 4

def chars_before_first_message(t : str):
    f = open(t)
    line = f.readlines()[0]
    for ii in range(len(line)-13):
        s = line[ii:ii+14]
        if unique(s):
            return ii + 14

def main():
    x = chars_before_first_packet("Day 6 Tuning Trouble/testinput.txt")
    print(x)
    x = chars_before_first_packet("Day 6 Tuning Trouble\input.txt")
    print(x)
    x = chars_before_first_message("Day 6 Tuning Trouble/testinput.txt")
    print(x)
    x = chars_before_first_message("Day 6 Tuning Trouble\input.txt")
    print(x)


if __name__ == "__main__":
    main()
