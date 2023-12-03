with open("2022/day1/input.txt") as f:
    lines = [line.strip() for line in f.readlines()]
    
    calories = []
    
    currentCalories = 0
    
    for line in lines:
        if line != '':
            currentCalories += int(line)
        else:
            calories.append(currentCalories)
            currentCalories = 0
        
    top3Calories = 0
    
    for i in range(3):
        maxVal = max(calories)
        top3Calories += maxVal
        calories.remove(maxVal)
    
    print(top3Calories)