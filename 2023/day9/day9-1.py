def predict(line: str) -> int:
    numbers = [*map(int, line.split())]
    
    lowerLevels, i = [numbers], 1
    while True:
        lowerLevels.append([])
        last = 0
        for idx, num in enumerate(lowerLevels[i - 1]):
            if idx == 0:
                last = num
                continue
            
            lowerLevels[i].append(num - last)
            last = num
            
        if all(x == 0 for x in lowerLevels[i]): break
        
        i += 1
        
    return sum([l[-1] for l in lowerLevels])

with open('2023/day9/input.txt', 'r') as f:
    lines = [l.strip() for l in f.readlines()]
    
    res = sum([predict(line) for line in lines])
    print(res)