def mapValues(to, start, length, seed):
    if seed >= start and seed < start + length:
        return seed + to - start
    return seed

with open('2023/day5/input.txt', 'r') as f:
    values = [[] for _ in range(8)]
    
    i, first = 0, True
    for idx, line in enumerate(f.readlines()):
        line = line.strip()
        
        if idx == 0:
            line = line.split(': ')[1]
            first = False
            
        if line == '':
            i += 1
            first = True
            continue
        
        if not first:
            values[i].append([*map(int, line.split())])
            
        first = False

    locations = []
    for i in range(0, len(values[0][0]), 2):
        value = values[0][0][i]
        length = values[0][0][i + 1]
        print(i)
        
        for val in range(value, value + length):
            seed = val
            for step in range(1, 1 + len(values) - 1):
                for map_ in values[step]:
                    temp = seed
                    seed = mapValues(*map_, temp)
                    if seed != temp: break
            locations.append(seed)
            
        for step in range(1, len(values))
    
    print(min(locations))