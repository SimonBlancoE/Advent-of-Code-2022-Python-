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


def is_touching(head_pos, tail_pos):
    head_x, head_y = head_pos[0], head_pos[1]
    tail_x, tail_y = tail_pos[0], tail_pos[1]
    adjacent_positions = [
        # Same spot
        head_pos == tail_pos,
        # Adjacent in x or y-axis
        head_x == tail_x + 1 and head_y == tail_y,
        head_x == tail_x - 1 and head_y == tail_y,
        head_x == tail_x and head_y == tail_y + 1,
        head_x == tail_x and head_y == tail_y - 1,
        # Adjacent in diagonals
        head_x == tail_x + 1 and head_y == tail_y + 1,
        head_x == tail_x + 1 and head_y == tail_y - 1,
        head_x == tail_x - 1 and head_y == tail_y + 1,
        head_x == tail_x - 1 and head_y == tail_y - 1,
    ]
    if any(adjacent_positions):
        return True
    else:
        return False


instructions = process_instructions()
print(instructions)

# Head movement
head = [(0, 0)]
tail = [(0, 0)]
move_head()
print(head)

for spot in head:
    if is_touching(spot, tail[0]):
        print(f"Head and Tail are touching at {spot} {tail[0]}")
    else:
        print(f"Head and Tail are not touching at {spot} {tail[0]}")


# Tail movement
visited_positions = set()
