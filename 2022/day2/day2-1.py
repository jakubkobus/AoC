with open("2022/day2/input.txt") as f:
    games = [line.strip().split(' ') for line in f.readlines()]
    
    points = {'X': 1, 'Y': 2, 'Z': 3}
    winConditions = {'A': 'Y', 'B': 'Z', 'C': 'X'}
    drawConditions = {'A': 'X', 'B': 'Y', 'C': 'Z'}
    
    totalScore = 0
    
    for game in games:
        opponent = game[0]
        me = game[1]
        if me == winConditions[opponent]:
            totalScore += points[me] + 6
        elif me == drawConditions[opponent]:
            totalScore += points[me] + 3
        else:
            totalScore += points[me]
    
    print(totalScore)