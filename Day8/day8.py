import numpy as np

with open('input', 'r') as file:
    data = [[int(char) for char in line.rstrip()] for line in file.readlines()]

data = np.array(data)


def look_north(index, item):
    print("looking north: ", data[:index[0], index[1]:index[1] + 1])
    if np.any(item <= data[:index[0], index[1]:index[1] + 1]):
        return False
    else:
        return True


def look_east(index, item):
    print("looking east: ", data[index[0]:index[0] + 1, index[1] + 1:])
    if np.any(item <= data[index[0]:index[0] + 1, index[1] + 1:]):
        return False
    else:
        return True


def look_west(index, item):
    print("looking west: ", data[index[0]:index[0] + 1, index[1] - 1::-1])
    if np.any(item <= data[index[0]:index[0] + 1, index[1] - 1::-1]):
        return False
    else:
        return True


def look_south(index, item):
    print("looking south: ", data[index[0] + 1:, index[1]: index[1] + 1])
    if np.any(item <= data[index[0] + 1:, index[1]: index[1] + 1]):
        return False
    else:
        return True



def exclude(index):
    if index[0] == 0 or index[1] == 0 or index[1] == data.shape[1] - 1 or index[0] == data.shape[0] - 1:
        return True


def count_visible_trees():
    count = 0
    for index, item in np.ndenumerate(data):
        if not exclude(index):
            print(index, item)
            if look_north(index, item) or look_south(index, item) or look_east(index, item) or look_west(index, item):
                count += 1
                print(f"Tree at position{index} with value {item} was counted")
        else:
            count += 1
            print(f"Tree at position{index} was counted for being at the perimeter")
    return count


print(count_visible_trees())

