def move(quantity: int, fromWhere: int, toWhere: int, stacks: list) -> list:
    for i in range(quantity):
        stacks[toWhere - 1].append(stacks[fromWhere - 1].pop())
        
    return stacks

def flipStacks(vert: list) -> list:
    stacks = [[] for s in range(9)]

    for stack in stacksVertical:
        index, spaceCount = 0, 1
        
        for char in stack:
            if char != '':
                stacks[index].append(char[1])
                index += 1
                spaceCount = 1
            else: spaceCount += 1
            
            if spaceCount % 5 == 0: 
                index, spaceCount = index + 1, 1
                
    for s in stacks: s.reverse()
    
    return stacks

with open("2022/day5/input.txt") as f: 
    stacksVertical = []
    
    for i in range(8):
        stacksVertical.append(f.readline().strip().split(' '))
    
    stacks = flipStacks(stacksVertical)

    for rl in range(2): f.readline()
    
    commands = []
    c = ' '
    while c:
        c = f.readline().strip().split()
        commandElements = []
        if c != []:
            commandElements.append(int(c[1]))
            commandElements.append(int(c[3]))
            commandElements.append(int(c[5]))
        commands.append(commandElements)
    commands.pop()

    for comm in commands:
        stacks = move(comm[0], comm[1], comm[2], stacks)
        
    answer = ''
    for s in stacks:
        answer += s[-1]
    
    print(answer)