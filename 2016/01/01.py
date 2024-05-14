'''
Deux essais pour résoudre le problème du jour 1.
'''
import os

def read_instructions(file_path):
    with open(file_path, 'r') as file:
        return file.read().strip().split(', ')

def calculate_distances(instructions):
    x, y = 0, 0
    dx, dy = 0, 1
    visited = {(x, y)}
    first_visited_twice = None
    for instruction in instructions:
        direction, steps = instruction[0], int(instruction[1:])
        if direction == 'R':
            dx, dy = dy, -dx
        else:
            dx, dy = -dy, dx
        for _ in range(steps):
            x, y = x + dx, y + dy
            if (x, y) in visited and first_visited_twice is None:
                first_visited_twice = abs(x) + abs(y)
            visited.add((x, y))
    return abs(x) + abs(y), first_visited_twice

instructions = read_instructions('01.txt')
final_distance, first_visited_twice_distance = calculate_distances(instructions)
print(final_distance)
print(first_visited_twice_distance)