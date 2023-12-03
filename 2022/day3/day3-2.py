def getPriorityOfItem(item: str) -> int:
    asciiIndex = ord(item)
    return asciiIndex - 38 if asciiIndex < 93 else asciiIndex - 96

def getSharingItem(rucksacks: list) -> str:
    for _, value in enumerate([*rucksacks[0]]):
        itemCount = [rucksack.count(value) for rucksack in rucksacks]
        
        if all(itemCount):
            return value

with open("2022/day3/input.txt") as f:
    lines = [line.strip() for line in f.readlines()]
    
    sumOfSharingItemsPriorities: int = 0
    
    for i in range(len(lines) // 3):
        sharingItem = getSharingItem([lines[i * 3], lines[i * 3 + 1], lines[i * 3 + 2]])
        sumOfSharingItemsPriorities += getPriorityOfItem(sharingItem)
    
    print(sumOfSharingItemsPriorities)