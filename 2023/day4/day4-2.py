import numpy as np

def fetchCardInfo(line: str) -> list:
    gameData = line.split(':')[1]
    pulled, winning = gameData.split('|')
    return [pulled.split(), winning.split()]

with open('2023/day4/sample.txt', 'r') as f:
    lines = [l.strip() for l in f.readlines()]
    cardsInfo = map(fetchCardInfo, lines)
    
    sum_ = 0
    
    for card in cardsInfo:
        matching = np.intersect1d(card[0], card[1])
        sum_ += (2 ** (len(matching) - 1)) if len(matching) > 0 else 0
    
    print(sum_)