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

with open('2023/day8/input.txt', 'r') as f:
    lines = [l.strip() for l in f.readlines()]
    
    ins = ['L', 'R']
    instructions = lines[0]
    steps = [*map(fetchStepData, lines[2:])]
    
    stepsCount, curr = 0, indexOf('AAA', steps)
    while True:
        nextElement = steps[curr].instructions[ins.index(instructions[stepsCount % len(instructions)])]
        curr = indexOf(nextElement, steps)
        if steps[curr].element == 'ZZZ': break
        stepsCount += 1
        
    print(stepsCount + 1)
        