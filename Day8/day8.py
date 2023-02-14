import numpy as np

with open('simput', 'r') as file:
    data = [[int(char) for char in line.rstrip()] for line in file.readlines()]

data = np.array(data)
print(type(data))
print(data)
print(data[1: -1, 1: -1])

inner_area = data[1: -1, 1: -1]
print(data)
dict = {}
for index, value in np.ndenumerate(data):
    print(index, value)
    dict[index] = value

print(dict)
right_boundary = len(data[0]) - 1
bottom_boundary = len(data) - 1
print(right_boundary)

for key, value in dict.items():
    if key[0] == 0 or key[0] == bottom_boundary:
        continue
    elif key[1] == 0 or key[1] == right_boundary:
        continue
    else:
        print(key, value)