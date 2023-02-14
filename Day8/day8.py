import numpy as np




with open('simput', 'r') as file:
    data = [[int(char) for char in line.rstrip()] for line in file.readlines()]

data = np.array(data)

inner_area = data[1: -1, 1: -1]

# iterate through every tree skipping the outer area
for index, item in np.ndenumerate(data):
    print(index, item)

# look north from position (5, 2)
print("North from 5,2: ", data[:5+1, 2:3])
# look north from (3, 2)
print("North from 3,2: ", data[:3+1, 2:3])
# look east from position (5, 2)
print("East from 5,2: ", data[5:, 2:])
# look west from position (5, 2)
print("West from 5,2: ", data[5: , :-2])
# look south from position (1, 3)
print("south from 1,3: ", data[1:, 3:4])
# look south from position (5, 2)
print("south from 5,2: ", data[5:, 2:3])

def look_north(index, item):
    print(item > data[:index[0]+1, index[1]:index[1]+1])

look_north((5,2), 3)

