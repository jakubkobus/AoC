with open('input.in', 'r') as f:
    lines = [list(map(int, l.strip().split('   '))) for l in f.readlines()]
    left, right = [i[0] for i in lines], [i[1] for i in lines]
    
    left.sort(); right.sort()
    diff = [abs(left[i] - right[i]) for i in range(len(left))]
    
    print(sum(diff))