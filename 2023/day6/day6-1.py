with open('2023/day6/input.txt', 'r') as f:
    lines = [l.strip() for l in f.readlines()]
    
    times = [*map(int, lines[0].split()[1:])]
    dists = [*map(int, lines[1].split()[1:])]
    
    result = 1
    
    for i in range(len(times)):
        waysToBeat = 0
        for j in range(1, times[i]):
            if dists[i] < ((times[i] - j) * j):
                waysToBeat += 1
        result *= waysToBeat
    
    print(result)