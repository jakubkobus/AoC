def isSafe(line: list[int]) -> bool:
    diff = line[1] - line[0]
    
    if abs(diff) not in [1, 2, 3]:
        return False
    
    if diff < 0:
        for i in range(2, len(line)):
            newDiff = line[i] - line[i - 1]
            if newDiff >= 0 or abs(newDiff) not in [1, 2, 3]:
                return False
        
        return True
    
    if diff > 0:
        for i in range(2, len(line)):
            newDiff = line[i] - line[i - 1]
            if newDiff <= 0 or newDiff not in [1, 2, 3]:
                return False
        
        return True
    
    return False
    
with open('input.in', 'r') as f:
    lines = [list(map(int, l.strip().split(' '))) for l in f.readlines()]
    print(sum(map(isSafe, lines)))