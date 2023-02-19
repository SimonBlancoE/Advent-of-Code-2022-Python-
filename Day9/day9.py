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


def negative_direction(direction, moves):
    if direction == 'D' or direction == 'L':
        return True
    else:
        return False


def determine_head_nxt_pos(direction, moves):
    if move_x(direction):
        if negative_direction(direction, moves):
            for _ in range(int(moves)):
                yield -1, 0
        else:
            for _ in range(int(moves)):
                yield 1, 0
    else:
        if negative_direction(direction, moves):
            for _ in range(int(moves)):
                yield 0, -1
        else:
            for _ in range(int(moves)):
                yield 0, 1


def move_head():
    for i in instructions:
        direction = i[0]
        moves = i[1]
        for x, y in determine_head_nxt_pos(direction, moves):
            current_x = head[-1][0]
            current_y = head[-1][1]
            head.append((current_x + x, current_y + y))





instructions = process_instructions()
print(instructions)

# Head movement
head = [(0, 0)]
tail = np.array([[0, 0]])
move_head()
print(head)

# Tail movement
visited_positions = set()
