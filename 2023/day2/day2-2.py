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
    
    sum_ = 0
    
    for game in games:
        sum_ += (max(game['red']) * max(game['green']) * max(game['blue']))
    
    print(sum_)