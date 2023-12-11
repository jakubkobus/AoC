raise NotImplementedError

import collections

MULTIPLIER = 1_000_000 - 1

#? https://stackoverflow.com/a/47902476 modified
def BFS(grid: list, start: tuple, end: tuple) -> int:
    queue = collections.deque([[start]])
    seen = set([start])
    width, height = len(grid[0]), len(grid)
    while queue:
        path = queue.popleft()
        x, y = path[-1]
        if end == (x, y):
            return len(path) - 1
        for x2, y2 in ((x+1,y), (x-1,y), (x,y+1), (x,y-1)):
            if 0 <= x2 < width and 0 <= y2 < height and (x2, y2) not in seen:
                queue.append(path + [(x2, y2)])
                seen.add((x2, y2))
                
def expandGalaxies(grid: list) -> list:
    emptyRows, emptyCols = [], []
    
    for idx, row in enumerate(grid):
        if all(char == '.' for char in row):
            emptyRows.append(idx)
    
    for colIdx in range(len(grid[0])):
        col = []
        for rowIdx in range(len(grid)):
            col.append(grid[rowIdx][colIdx])
        if all(char == '.' for char in col):
            emptyCols.append(colIdx)
            
    for idx, emptyRow in enumerate(emptyRows):
        for _ in range(MULTIPLIER):
            grid.insert(emptyRow + idx * MULTIPLIER, grid[emptyRow + idx * MULTIPLIER])
    
    grid = [[*row] for row in grid]
    
    for idx, emptyCol in enumerate(emptyCols):
        for rowIdx in range(len(grid)):
            for _ in range(MULTIPLIER):
                grid[rowIdx].insert(emptyCol + idx * MULTIPLIER, '.')
    
    return [''.join(row) for row in grid]

def getGalaxiesPos(grid: list) -> list:
    res = []
    
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] == '#':
                res.append((x, y))
    
    return res

with open('2023/day11/sample.txt', 'r') as f:
    #* All pairs = (n * (n - 1)) // 2
    
    grid = [l.strip() for l in f.readlines()]
    grid = expandGalaxies(grid)
    galaxiesPos = getGalaxiesPos(grid)
    
    result = 0
    
    donePairs = []
    for idx, pos1 in enumerate(galaxiesPos):
        for pos2 in galaxiesPos:
            if pos1 == pos2 or sorted([pos1, pos2]) in donePairs: continue
            result += BFS(grid, pos1, pos2)
            donePairs.append(sorted([pos1, pos2]))
                
    print(result) #! ~infinite