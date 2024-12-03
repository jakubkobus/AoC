import re

with open('input.in', 'r') as f:
    lines = [l.strip() for l in f.readlines()]
    
    result = []
    for l in lines:
        string = ""
        enabled = True
        for c in l:
            string += c
            
            dont = re.search(r'don\'t\(\)', string)
            if dont:
                string = ""
                enabled = False
                
            do = re.search(r'do\(\)', string)
            if do:
                string = ""
                enabled = True
                
            mul = re.search(r'mul\(([0-9]+),([0-9]+)\)', string)
            if mul:
                string = ""
                if enabled:
                    result.append(mul.groups())
                    print('added', mul.groups())
    
    sum_ = 0
    for r in result:
        sum_ += int(r[0]) * int(r[1])
    print(sum_)