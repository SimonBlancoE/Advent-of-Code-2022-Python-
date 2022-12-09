print("Hello")
calories = 0
max_calories = 0
with open("input.txt", 'r') as input:
    lines = input.readlines()
    for line in lines:
        if line.strip():
            calories += int(line.strip())
        else:
            if calories > max_calories:
                max_calories = calories
            calories = 0
                
print(max_calories)
