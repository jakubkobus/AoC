def toBinary(n, length):
    return bin(n)[2:].zfill(length)

with open('input.in', 'r') as f:
    lines = [l.strip() for l in f.readlines()]
    
    result = []
    components = []
    
    final = 0
    
    for l in lines:
        a, b = l.split(':')
        result.append(int(a))
        components.append(list(map(int, b.strip().split(' '))))
    
    for i, r in enumerate(result):
        options = 2**(len(components[i]) - 1)
        
        for o in range(options):
            binary = toBinary(o, len(components[i]) - 1)
            res = components[i][0]
            
            for j, c in enumerate(components[i][1:]):
                if binary[j] == '1':
                    res += c
                else:
                    res *= c
            
            if res == r:
                final += r
                break
            
    print(final)
                