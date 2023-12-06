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
    for value in values[0][0]:
        seed = value
        for step in range(1, len(values)):
            for map_ in values[step]:
                temp = seed
                seed = mapValues(*map_, temp)
                if seed != temp: break
        locations.append(seed)
    
    print(min(locations))