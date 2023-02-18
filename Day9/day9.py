import numpy as np


def process_instructions():
    with open('simput', 'r') as f:
        data = [(line.strip()[0], line.strip()[-1]) for line in f.readlines()]
        return data


def move_x(direction):
    if direction == 'R' or direction == 'L':
        return True
    elif direction == 'U' or direction == 'D':
        return False


def set_moves(direction, moves):
    if direction == 'D' or direction == 'L':
        return moves * -1
    else:
        return moves


def determine_head_direction(current_pos, direction, moves):
    if move_x(direction):
        return current_pos[0] + set_moves(direction, moves), current_pos[1]
    else:  # move y
        return current_pos[0], current_pos[1] + set_moves(direction, moves)


def move_head():
    for i in instructions:
        head_current = head[-1]
        print(head_current)
        inst_direction, inst_moves = i[0], int(i[1])
        new = determine_head_direction(head_current, inst_direction, inst_moves)
        head.append(new)


instructions = process_instructions()
print(instructions)

# Head movement
head = [(0, 0)]
tail = np.array([[0, 0]])
move_head()
print(head)

# Tail movement
visited_positions = set()
