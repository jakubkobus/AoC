import numpy as np

def fetchCardInfo(line: str) -> list:
    gameData = line.split(':')[1]
    pulled, winning = gameData.split('|')
    return [pulled.split(), winning.split()]

with open('2023/day4/input.txt', 'r') as f:
    lines = [l.strip() for l in f.readlines()]
    cardsInfo = map(fetchCardInfo, lines)
    
    cardInstances = [1 for _ in range(len(lines))]
    
    for idx, card in enumerate(cardsInfo):
        matching = np.intersect1d(card[0], card[1])
        for _ in range(cardInstances[idx]):
            for i in range(idx, idx + len(matching)):
                cardInstances[i + 1] += 1
    
    print(sum(cardInstances))