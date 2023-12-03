def fetchGameInfo(line: str) -> dict:
    _, info = line.split(':')
    games = info.split(';')
    games = [game.split(',') for game in games]
    
    gameInfo = {
        'red': [],
        'green': [],
        'blue': []
    }
    
    for game in games:
        for cube in game:
            if 'red' in cube:
                gameInfo['red'].append(int(cube[:-3].strip()))
            if 'green' in cube:
                gameInfo['green'].append(int(cube[:-5].strip()))
            if 'blue' in cube:
                gameInfo['blue'].append(int(cube[:-4].strip()))
    
    return gameInfo

with open('2023/day2/input.txt', 'r') as f:
    lines = [l.strip() for l in f.readlines()]
    games = [*map(fetchGameInfo, lines)]
    
    assumptions = {
        'red': 12,
        'green': 13,
        'blue': 14
    }
    
    sum_ = 0
    
    for idx, game in enumerate(games):
        possible = True
        
        for color in game:
            pulled = game[color]
            
            for pulledOnce in pulled:
                if pulledOnce > assumptions[color]:
                    possible = False
        
        if possible: sum_ += idx + 1
    
    print(sum_)