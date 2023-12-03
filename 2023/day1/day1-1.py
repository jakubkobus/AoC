def filterDigits(line: str) -> str:
    filtered = ''
    for c in line:
        if c.isdigit():
            filtered += c
    return filtered

with open('2023/day1/input.txt', 'r') as f:
    lines = [l.strip() for l in f.readlines()]
    lines = [*map(filterDigits, lines)]
    
    sum_ = 0
    
    for line in lines:
        sum_ += int(line[0]) * 10 + int(line[-1])
        
    print(sum_)