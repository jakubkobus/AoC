class Vec2:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def __repr__(self):
        return f"[{self.x}, {self.y}]"

class Token:
    def __init__(self, pos: Vec2, token: str):
        self.pos = pos
        self.token = token
        self.length = len(self.token)
        self.neighbours = None
        
        if self.token.isdecimal(): self.token = int(self.token)
        
    def calculateNeighbours(self):
        self.neighbours = [Vec2(self.pos.x + i, self.pos.y + j) for i in range(-1, self.length + 1) for j in range(-1, 2, 2)]
        self.neighbours.append(Vec2(self.pos.x -           1, self.pos.y))
        self.neighbours.append(Vec2(self.pos.x + self.length, self.pos.y))
        
    def __repr__(self):
        typeOf = str(type(self.token)).split("'")[1]
        return f"[{self.pos.x}, {self.pos.y}] {typeOf}({self.token})"
            
def fetchLineInfo(line: str, row: int) -> dict:
    digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    BLANK = '.'
    info = []
    
    token, last, start = '', BLANK, None
    for idx, char in enumerate(line):
        if last == BLANK and char != BLANK:
            token += char
            start = idx
            last = char
            
            if char not in digits:
                info.append(Token(Vec2(start, row), token))
                info[-1].calculateNeighbours()
                token = ''
                last = BLANK
                
            if idx + 1 == len(line):
                info.append(Token(Vec2(start, row), token))
                info[-1].calculateNeighbours()
            
            continue
        
        if char != BLANK:
            if char not in digits:
                info.append(Token(Vec2(start, row), token))
                info[-1].calculateNeighbours()
                info.append(Token(Vec2(start + info[-1].length, row), char))
                info[-1].calculateNeighbours()
                token = ''
                last = BLANK
                continue
            
            token += char
            last = char
            
            if idx + 1 == len(line):
                info.append(Token(Vec2(start, row), token))
                info[-1].calculateNeighbours()
            
            continue
            
        if last != BLANK and char == BLANK:
            info.append(Token(Vec2(start, row), token))
            info[-1].calculateNeighbours()
            last = char
            token = ''
            continue
    
    return info

def indexOutOfRange(vec: Vec2, width: int, height: int) -> bool:
    return vec.x < 0 or vec.x >= width or vec.y < 0 or vec.y >= height

def isValid(token: str, lines: list) -> bool:
    if not isinstance(token.token, int): return False
    
    BLANK = '.'
    valid = False
    
    for neighbour in token.neighbours:
        if indexOutOfRange(neighbour, len(lines[0]), len(lines)): continue
        if lines[neighbour.y][neighbour.x] != BLANK:
            valid = True
            break
    
    return valid

with open('2023/day3/input.txt', 'r') as f:
    lines = [l.strip() for l in f.readlines()]

    tokens = []
    for idx, line in enumerate(lines):
        tokens.append(fetchLineInfo(line, idx))
        print(tokens[-1])
    
    sum_ = 0
    for lineTokens in tokens:
        for token in lineTokens:
            if isValid(token, lines):
                sum_ += token.token
                
    print(sum_)