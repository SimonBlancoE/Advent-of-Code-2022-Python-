import numpy as np

with open('input', 'r') as file:
    data = [[int(char) for char in line.rstrip()] for line in file.readlines()]

data = np.array(data)


# Part 1 Functions
def plot_tree_lines(index, item):
    trees_north = data[:index[0], index[1]:index[1] + 1]
    trees_east = data[index[0]:index[0] + 1, index[1] + 1:]
    trees_west = data[index[0]:index[0] + 1, index[1] - 1::-1]
    trees_south = data[index[0] + 1:, index[1]: index[1] + 1]
    trees_in_axis = [trees_north, trees_east, trees_west, trees_south]
    trees_in_axis = [np.squeeze(trees) for trees in trees_in_axis]
    return trees_in_axis


def tree_is_visible(index, item):
    trees_in_axis = plot_tree_lines(index, item)
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


# Part 2 Functions
def count_trees(tree, tree_line):
    count = 0
    tree_line = tree_line.flatten()
    for trees in tree_line:
        count += 1
        if tree <= trees:
            break
    return count


def measure_viewing_distance():
    viewing_distance = 1
    viewing_distance_scores = []
    for index, item in np.ndenumerate(data):
        if not exclude_from_comparison(index):
            trees_in_axis = plot_tree_lines(index, item)
            trees_in_axis[0] = np.flip(trees_in_axis[0])    # Reverse array looking north
            for tree_line in trees_in_axis:
                count = count_trees(item, tree_line)
                viewing_distance *= count
            viewing_distance_scores.append(viewing_distance)
            viewing_distance = 1
    return max(viewing_distance_scores)


# Part 1
print(count_visible_trees())

# Part 2
print(measure_viewing_distance())
