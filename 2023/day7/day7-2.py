from itertools import chain

def getType(hand: str) -> int:
    dct = {}
    for c in hand:
        if dct.get(c) == None: dct[c] = 1
        else: dct[c] += 1
    
    cnts = [0, 0, 0, 0, 0]
    for key in dct:
        for cnt in range(5):
            if dct[key] == cnt + 1: cnts[cnt] += 1
    
    if 'J' in hand:
        maxHand, bestOption = 0, ''
        for c in 'AKQT98765432':
            type_ = getType(hand.replace('J', c))
            if type_ > maxHand:
                maxHand = type_
                bestOption = c
                
        return maxHand
    
    res = [[5, 0, 0, 0, 0], #? 0 - High card
           [3, 1, 0, 0, 0], #? 1 - One pair
           [1, 2, 0, 0, 0], #? 2 - Two pair
           [2, 0, 1, 0, 0], #? 3 - Three of a kind
           [0, 1, 1, 0, 0], #? 4 - Full house
           [1, 0, 0, 1, 0], #? 5 - Four of a kind
           [0, 0, 0, 0, 1]] #? 6 - Five of a kind
        
    return res.index(cnts)

with open('2023/day7/input.txt', 'r') as f:
    lines = [l.strip() for l in f.readlines()]
    
    ranks = [[] for _ in range(7)]
    for line in lines:
        hand, bid = line.split()
        ranks[getType(hand)].append({'hand': hand, 'bid': int(bid)})
    
    key = 'AKQT98765432J'
    for idx, rank in enumerate(ranks):
        ranks[idx] = sorted(rank, key=lambda w: [key.index(c) for c in w['hand']], reverse=True)
    
    ranks, total = chain.from_iterable(ranks), 0
    for idx, rank in enumerate(ranks):
        total += (idx + 1) * rank['bid']
    
    print(total)