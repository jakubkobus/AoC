with open('2023/day6/input.txt', 'r') as f:
    lines = [l.strip() for l in f.readlines()]
    
    time = int(''.join(lines[0].split()[1:]))
    dist = int(''.join(lines[1].split()[1:]))
    
    waysToBeat = 1
    for i in range(1, time):
        if dist < ((time - i) * i):
            waysToBeat += time - i
            break
        
    for j in range(time - 1, -1, -1):
        if dist < ((time - j) * j):
            waysToBeat -= time - j
            break
    
    print(waysToBeat)