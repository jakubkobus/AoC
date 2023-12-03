def splitRange(element: list) -> list:
    return [*map(int, element[0].split('-'))] + [*map(int, element[1].split('-'))]

def conditionCheck(ranges: list) -> bool:
    if ranges[1] < ranges[2]:
        return False
    
    if ranges[3] < ranges[0]:
        return False
    
    return True

with open("2022/day4/input.txt") as f:
    lines = [line.strip().split(',') for line in f.readlines()]
    lines = map(splitRange, lines)
    good = [*map(conditionCheck, lines)].count(True)
    print(good)