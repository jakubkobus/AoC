raise NotImplementedError

from itertools import chain

class Vec2:
    def __init__(self, x, y):
        self.x = x 
        self.y = y
        
    def __repr__(self):
        return f"[{self.x}, {self.y}]"
    
def getStartPos(board: list) -> Vec2:
    for y in range(len(board)):
        for x in range(len(board[y])):
            if board[y][x] == 'S': return Vec2(x, y)
    return Vec2(-1, -1)

def getStartingNodes(pos: Vec2, board: list) -> list:   
    ret = []
    
    for adder in range(-1, 2, 2):
        if adder == -1 and board[pos.y + adder][pos.x] in ['7', 'F', '|']:
            ret.append(Vec2(pos.x, pos.y + adder))
        if adder == 1 and board[pos.y + adder][pos.x] in ['L', 'J', '|']:
            ret.append(Vec2(pos.x, pos.y + adder))
        if adder == -1 and board[pos.y][pos.x + adder] in ['F', 'L', '-']:
            ret.append(Vec2(pos.x + adder, pos.y))
        if adder == 1 and board[pos.y][pos.x + adder] in ['J', '7', '-']:
            ret.append(Vec2(pos.x + adder, pos.y))
                
    return ret

def getLastDir(pos: Vec2, last: Vec2) -> int:
    if pos.x == last.x:
        return 0 if (pos.y - last.y) == 1 else 2
    if pos.y == last.y:
        return 3 if (pos.x - last.x) == 1 else 1
    return -1

with open('2023/day10/sample.txt', 'r') as f:
    #? board[y][x] = chr
    board = [l.strip() for l in f.readlines()]
    width, height = len(board[0]), len(board)
    visited = [[0 for _ in range(width)] for _ in range(height)]
    nodes = []
    
    start: Vec2 = getStartPos(board)
    visited[start.y][start.x] = 1
    
    startingNodes = getStartingNodes(start, board)
    
    dirs = {
        '7': [3, 2], #!   N
        'J': [0, 3], #! W   E
        'L': [0, 1], #!   S
        'F': [2, 1], #!   0
        '-': [3, 1], #! 3   1
        '|': [0, 2]  #!   2
    }
    
    for idx, node in enumerate(startingNodes):
        last = start
        curr = node
        while True:
            visited[curr.y][curr.x] = visited[last.y][last.x] + 1
            currChr = board[curr.y][curr.x]
            available = dirs[currChr]
            lastDir = getLastDir(curr, last)
            nextDir = available[(available.index(lastDir) + 1) % 2]
            last = Vec2(curr.x, curr.y)
            if nextDir == 0: curr.y -= 1
            if nextDir == 1: curr.x += 1
            if nextDir == 2: curr.y += 1
            if nextDir == 3: curr.x -= 1
            if board[curr.y][curr.x] not in dirs: break
            
        nodes.append(visited)
        visited = [[0 for _ in range(width)] for _ in range(height)]
        visited[start.y][start.x] = 1
            
    result = [[0 for _ in range(width)] for _ in range(height)]
    for n in nodes:
        for y in range(len(n)):
            for x in range(len(n[y])):
                result[y][x] += n[y][x]
                
    print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in result]))
    
    chained = [*chain.from_iterable(result)]
    maxNum = max(chained)
    count = chained.count(maxNum)
    
    print(count // 2 + 1 if count > 1 else maxNum)