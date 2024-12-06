from enum import Enum

class Direction(Enum):
    UP = 1
    RIGHT = 2
    DOWN = 3
    LEFT = 4

def locateGuard(lines: list[str]) -> list[int]:
    for y in range(len(lines)):
        for x in range(len(lines[y])):
            if lines[y][x] == '^':
                return [x, y]
    return [-1, -1]

with open('input.in', 'r') as f:
    minimap = [l.strip() for l in f.readlines()]
    start = locateGuard(minimap)
    visited = [[start[0], start[1]]]
    
    minimap2 = []
    for y in range(len(minimap)):
        minimap2.append('')
        for x in range(len(minimap[y])):
            if minimap[y][x] == '^':
                minimap2[y] += '.'
            else:
                minimap2[y] += minimap[y][x]
    
    minimap = minimap2
    
    
    directions = [Direction.UP, Direction.RIGHT, Direction.DOWN, Direction.LEFT]
    directionIndex = 0
    pos = start
    direction = directions[directionIndex]
    while (0 <= pos[1] < len(minimap[0])) and (0 <= pos[0] < len(minimap)): 
        if minimap[pos[1]][pos[0]] != '.':
            if direction == Direction.UP: pos[1] += 1
            if direction == Direction.RIGHT: pos[0] -= 1
            if direction == Direction.DOWN: pos[1] -= 1
            if direction == Direction.LEFT: pos[0] += 1

            directionIndex = (directionIndex + 1) % 4
            direction = directions[directionIndex]
        
        if pos not in visited:
            visited.append([pos[0], pos[1]])
            
        if direction == Direction.UP: pos[1] -= 1
        if direction == Direction.RIGHT: pos[0] += 1
        if direction == Direction.DOWN: pos[1] += 1
        if direction == Direction.LEFT: pos[0] -= 1
            
    print(len(visited))
    