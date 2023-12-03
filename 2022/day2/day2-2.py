with open("2022/day2/input.txt") as f:
    games = [line.strip().split(' ') for line in f.readlines()]
    
    points = {'X': 1, 'Y': 2, 'Z': 3}
    winConditions = {'A': 'Y', 'B': 'Z', 'C': 'X'}
    drawConditions = {'A': 'X', 'B': 'Y', 'C': 'Z'}
    loseConditions = {'A': 'Z', 'B': 'X', 'C': 'Y'}
    
    totalScore = 0
    
    for game in games:
        opponent = game[0]
        condition = game[1]

        if condition == 'X':
            myMove = loseConditions[opponent]
            totalScore += points[myMove]
        if condition == 'Y':
            myMove = drawConditions[opponent]
            totalScore += points[myMove] + 3
        if condition == 'Z':
            myMove = winConditions[opponent]
            totalScore += points[myMove] + 6

    print(totalScore)