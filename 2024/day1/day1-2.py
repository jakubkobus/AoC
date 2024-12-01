with open('input.in', 'r') as f:
    lines = [list(map(int, l.strip().split('   '))) for l in f.readlines()]
    left, right = [i[0] for i in lines], [i[1] for i in lines]
    
    sum_ = 0
    for val in left:
        sum_ += val * right.count(val)
    
    print(sum_)