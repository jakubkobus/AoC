checkRange = 4

with open("2022/day6/input.txt") as f:
    line = f.readline().strip()

    lastFour = []

    for index, char in enumerate(line, start = 1):
        lastFour.append(char)

        if len(lastFour) > checkRange:
            lastFour.pop(0)
        
        if len([*set(lastFour)]) == checkRange:
            print(index)
            break