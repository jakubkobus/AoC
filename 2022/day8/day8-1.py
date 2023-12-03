def isVisible(row: int, col: int, grid: list) -> bool:
    height = int(grid[row][col])
    
    top_bottom = [True, True]
    idx = 0
    
    for rowIndex in range(len(grid)):
        if rowIndex == row:
            idx = 1
            continue
        
        currentHeight = int(grid[rowIndex][col])
        
        if currentHeight >= height:
            top_bottom[idx] = False

    left_right = [True, True]
    idx = 0
    
    for colIndex in range(len(grid[row])):
        if colIndex == col:
            idx = 1
            continue
        
        currentHeight = int(grid[row][colIndex])
        
        if currentHeight >= height:
            left_right[idx] = False
            
    visibility = top_bottom + left_right
    
    return any(visibility)    
            

with open('2022/day8/input.txt') as f:
    grid = [line.strip() for line in f.readlines()]
    
    visibleTrees = 0
    
    for rowIndex, _ in enumerate(grid):
        for colIndex, _ in enumerate(grid[rowIndex]):
            if isVisible(rowIndex, colIndex, grid):
                visibleTrees += 1
                
    print(visibleTrees)