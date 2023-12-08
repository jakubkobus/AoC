from math import lcm

class Step:
    def __init__(self, element, left, right):
        self.element = element
        self.instructions = [left, right]

def fetchStepData(step: str) -> Step:
    return Step(*step
                .replace('(', '')
                .replace(')', '')
                .replace('=', '')
                .replace(',', '')
                .split())

def indexOf(element: str, steps: list) -> int:
    for idx, step in enumerate(steps):
        if step.element == element:
            return idx
    return -1

def getStepsA(steps: list) -> list:
    res = []
    for step in steps:
        if step.element.endswith('A'): res.append(step)
    return res

def zIdx(lst: list) -> bool:
    for i, e in enumerate(lst):
        if e['element'].endswith('Z'): return i
    return -1

with open('2023/day8/input.txt', 'r') as f:
    lines = [l.strip() for l in f.readlines()]
    
    ins = ['L', 'R']
    instructions = lines[0]
    steps = [*map(fetchStepData, lines[2:])]
    
    stepsA = getStepsA(steps)
    loop = [[] for _ in range(len(stepsA))]
    loopTo = [0 for _ in range(len(stepsA))]
    
    for idx, step in enumerate(stepsA):
        curr = steps.index(step)
        i = 0
        while True:
            temp = {'element': steps[curr].element, 'insIdx': i % len(instructions)}
            
            if temp in loop[idx]:
                loopTo[idx] = loop[idx].index(temp)
                break
            else: loop[idx].append(temp)
            
            nextElement = steps[curr].instructions[ins.index(instructions[i % len(instructions)])]
            curr = indexOf(nextElement, steps)
            i += 1

    zIdxs = [zIdx(l) for l in loop]
    print(lcm(*zIdxs)) #! Thanks to https://github.com/makes
        
    
    