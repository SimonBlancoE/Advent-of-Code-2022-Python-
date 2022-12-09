all_cal = []
calories = 0

with open("input.txt", 'r') as input:
    lines = input.readlines()
    for line in lines:
        if line.strip():
            calories += int(line.strip())
            #print (calories)
        else:
            all_cal.append(calories)
            calories = 0
            #print (top_three)

all_cal.sort()
top_three = all_cal[-3:]
print (sum(top_three))

            
