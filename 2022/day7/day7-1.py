class Directory:
    def __init__(self, name):
        self.name = name
        self.size = 0
        self.parent = None
        self.children = []
    
with open("2022/day7/input.txt") as f:
    lines = [line.strip().split() for line in f.readlines()]
    
    mainDirectory = Directory('/')
    
    currentDirectory = mainDirectory
    lastDir = None
    dirCount = 1
    
    for index, line in enumerate(lines):
        if index == 0:
            continue
        
        if line[0:2] == ['$', 'cd']:
            if line[2] == '..':
                currentDirectory = currentDirectory.parent
            else:
                newDir = Directory(line[2])
                newDir.parent = currentDirectory
                currentDirectory.children.append(newDir)
                currentDirectory = newDir
                dirCount += 1
                lastDir = newDir
                
            continue
            
        if line[0] not in ['$', 'dir']:
            currentDirectory.size += int(line[0])
            currentDirectory.children.append(f"F({line[1]})")
            helper = currentDirectory
            
            while helper.parent != None:
                helper.parent.size += int(line[0])
                helper = helper.parent
                
    directories = []
    
    currentDirectory = mainDirectory
    
    while currentDirectory != lastDir:
        if currentDirectory not in directories:
            directories.append(currentDirectory)
        
        for _, child in enumerate(currentDirectory.children):
            if isinstance(child, Directory):
                if child not in directories:
                    currentDirectory = child
                    break
        else:
            currentDirectory = currentDirectory.parent
            
    directories.append(lastDir)
    
    sizeSum = 0
    
    for directory in directories:
        if directory.size <= 100_000:
            sizeSum += directory.size
            
    print(sizeSum)