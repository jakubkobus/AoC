def splitLine(line: str) -> tuple:
    halfIndex = len(line) // 2
    return (line[:halfIndex], line[halfIndex:])

def getPriorityOfSharingItem(rucksackContent: str) -> int:
    compartment1, compartment2 = splitLine(rucksackContent)
    
    for _, value1 in enumerate([*compartment1]):
        for _, value2 in enumerate([*compartment2]):
            if value1 == value2:
                asciiIndex = ord(value1)
                return asciiIndex - 38 if asciiIndex < 93 else asciiIndex - 96

with open("2022/day3/input.txt") as f:
    lines = [line.strip() for line in f.readlines()]
    
    sumOfSharingItemsPriorities: int = 0
    
    for line in lines:
        sumOfSharingItemsPriorities += getPriorityOfSharingItem(line)
    
    print(sumOfSharingItemsPriorities)