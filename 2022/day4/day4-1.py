def splitRange(element: list) -> list:
    return [*map(int, element[0].split('-'))] + [*map(int, element[1].split('-'))]

def conditionCheck(ranges: list) -> bool:
    if ranges[0] <= ranges[2] and ranges[1] >= ranges[3]:
        return True
    
    if ranges[2] <= ranges[0] and ranges[3] >= ranges[1]:
        return True
    
    return False

with open("2022/day4/input.txt") as f:
    lines = [line.strip().split(',') for line in f.readlines()]
    lines = map(splitRange, lines)
    good = [*map(conditionCheck, lines)].count(True)
    print(good)