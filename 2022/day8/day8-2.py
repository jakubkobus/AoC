def calculateScenicScore(row: int, col: int, grid: list) -> bool:
    if row == 0 or row == len(grid) - 1 or col == 0 or col == len(grid[row]) - 1:
        return 0
    
    height = int(grid[row][col])
    
    top = 0
    for rowIdx in range(row - 1, -1, -1):
        currentHeight = int(grid[rowIdx][col])
        if currentHeight < height:
            top += 1
        else:
            top += 1
            break
    
    right = 0
    for colIdx in range(col + 1, len(grid[row])):
        currentHeight = int(grid[row][colIdx])
        if currentHeight < height:
            right += 1
        else:
            right += 1
            break
    
    bottom = 0
    for rowIdx in range(row + 1, len(grid)):
        currentHeight = int(grid[rowIdx][col])
        if currentHeight < height:
            bottom += 1
        else:
            bottom += 1
            break
    
    left = 0
    for colIdx in range(col - 1, -1, -1):
        currentHeight = int(grid[row][colIdx])
        if currentHeight < height:
            left += 1
        else:
            left += 1
            break
    
    return top * right * bottom * left

with open('2022/day8/input.txt') as f:
    grid = [line.strip() for line in f.readlines()]
    
    highestScenicScore = 0
    
    for rowIndex, _ in enumerate(grid):
        for colIndex, _ in enumerate(grid[rowIndex]):
            score = calculateScenicScore(rowIndex, colIndex, grid)
            if score > highestScenicScore:
                highestScenicScore = score
            
    print(highestScenicScore)