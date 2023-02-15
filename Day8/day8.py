import numpy as np

with open('input', 'r') as file:
    data = [[int(char) for char in line.rstrip()] for line in file.readlines()]

data = np.array(data)


def tree_is_visible(index, item):
    trees_north = data[:index[0], index[1]:index[1] + 1]
    trees_east = data[index[0]:index[0] + 1, index[1] + 1:]
    trees_west = data[index[0]:index[0] + 1, index[1] - 1::-1]
    trees_south = data[index[0] + 1:, index[1]: index[1] + 1]
    trees_in_axis = [trees_north, trees_east, trees_west, trees_south]
    trees_in_axis = [np.squeeze(trees) for trees in trees_in_axis]

    for trees in trees_in_axis:
        if np.all(item > trees):
            return True
    return False


def exclude_from_comparison(index):
    if index[0] == 0 or index[1] == 0 or index[1] == data.shape[1] - 1 or index[0] == data.shape[0] - 1:
        return True


def count_visible_trees():
    count = 0
    for index, item in np.ndenumerate(data):
        if not exclude_from_comparison(index):
            if tree_is_visible(index, item):
                count += 1
        else:
            count += 1
    return count


print(count_visible_trees())
