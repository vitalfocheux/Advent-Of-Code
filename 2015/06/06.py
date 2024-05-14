'''
Un essai pour résoudre le jour 6 de l'année 2015
'''

import re
import numpy as np

def read_instructions(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file]

def part1(instructions):
    grid = np.zeros((1000, 1000), dtype=bool)  # Change here
    for instruction in instructions:
        action, x1, y1, x2, y2 = re.match(r'(turn on|turn off|toggle) (\d+),(\d+) through (\d+),(\d+)', instruction).groups()
        x1, y1, x2, y2 = map(int, [x1, y1, x2, y2])
        if action == 'turn on':
            grid[x1:x2+1, y1:y2+1] = True
        elif action == 'turn off':
            grid[x1:x2+1, y1:y2+1] = False
        elif action == 'toggle':
            grid[x1:x2+1, y1:y2+1] = ~grid[x1:x2+1, y1:y2+1]
    return np.sum(grid)

def part2(instructions):
    grid = np.zeros((1000, 1000), dtype=int)
    for instruction in instructions:
        action, x1, y1, x2, y2 = re.match(r'(turn on|turn off|toggle) (\d+),(\d+) through (\d+),(\d+)', instruction).groups()
        x1, y1, x2, y2 = map(int, [x1, y1, x2, y2])
        if action == 'turn on':
            grid[x1:x2+1, y1:y2+1] += 1
        elif action == 'turn off':
            grid[x1:x2+1, y1:y2+1] = np.maximum(grid[x1:x2+1, y1:y2+1] - 1, 0)
        elif action == 'toggle':
            grid[x1:x2+1, y1:y2+1] += 2
    return np.sum(grid)

instructions = read_instructions('06.txt')

# Part 1
print(part1(instructions))

# Part 2
print(part2(instructions))