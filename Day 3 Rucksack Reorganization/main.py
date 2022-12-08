
def convert_to_priority(ii : str):
    if ii.islower():
        return ord(ii) - 96   
    if ii.isupper():
        return ord(ii) - 96 + 32 + 26

def calculate_priority_sum(t):
    f = open(t)
    lines = f.readlines()
    sum = 0
    break_bool = False
    for line in lines:
        line = line.strip()
        length = len(line)
        for ii in line[:int(length/2)]:
            for jj in line[int(length/2):]:
                if ii == jj:
                    sum += convert_to_priority(ii)
                    break_bool = True
                    break
            if break_bool:
                break
        break_bool = False
            
    f.close()
    return sum

def calculate__badge_priority_sum(t):
    f = open(t)
    lines = f.readlines()
    sum = 0
    break_bool = False
    for line_num in range(len(lines)):
        if line_num % 3 == 0:
            for ii in lines[line_num]:
                for jj in lines[line_num+1]:
                    if ii == jj:
                        for kk in lines[line_num+2]:
                            if ii == jj == kk:
                                sum += convert_to_priority(ii)
                                
                                break_bool = True
                                break
                    if break_bool:
                        break
                if break_bool:
                    break
            break_bool = False
            
    f.close()
    return sum


def main():
    x = calculate_priority_sum("Day 3 Rucksack Reorganization\input.txt")
    print(x)

    x = calculate__badge_priority_sum("Day 3 Rucksack Reorganization\\input.txt")
    print(x)

main()
