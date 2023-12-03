def filterDigits(line: str) -> str:
    filtered = ''
    for c in line:
        if c.isdigit():
            filtered += c
    return filtered

def repairDigits(line: str) -> str:
    digits = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    digit = ''
    start = 0
    out = ''
    for c in line:
        if c.isdigit():
            out += c
            continue
        
        digit += c
        for i in range(len(digits)):
            if digits[i] in digit:
                out += str(i + 1)
                digit = digit[-1]
                break
            
    return out

# Part 2
with open('2023/day1/input.txt', 'r') as f:
    lines = [l.strip() for l in f.readlines()]
    lines = [*map(repairDigits, lines)]
    lines = [*map(filterDigits, lines)]
    
    sum_ = 0
    
    for line in lines:
        sum_ += int(line[0]) * 10 + int(line[-1])
        
    print(sum_)