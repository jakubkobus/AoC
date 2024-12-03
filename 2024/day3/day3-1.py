import re

with open('input.in', 'r') as f:
    lines = [l.strip() for l in f.readlines()]
    
    result = 0
    for l in lines:
        matches = re.findall(r'mul\(([0-9]+),([0-9]+)\)', l)
        for m in matches:
            result += int(m[0]) * int(m[1])
    
    print(result)