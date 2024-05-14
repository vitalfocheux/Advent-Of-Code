'''
Dix essais pour résoudre le jour 23 de l'Avent de Code 2018
'''
import re
from scipy.optimize import linprog
from queue import PriorityQueue

def parse_input(input_lines):
    nanobots = []
    for line in input_lines:
        x, y, z, r = map(int, re.findall(r'-?\d+', line))
        nanobots.append(((x, y, z), r))
    return nanobots

def part1(nanobots):
    (x_max, y_max, z_max), r_max = max(nanobots, key=lambda x: x[1])
    return sum(1 for (px, py, pz), pr in nanobots if abs(px - x_max) + abs(py - y_max) + abs(pz - z_max) <= r_max)

def part2(nanobots):
    q = PriorityQueue()
    for (x, y, z), r in nanobots:
        d = abs(x) + abs(y) + abs(z)
        q.put((max(0, d - r),1))
        q.put((d + r + 1,-1))
    count = max_count = max_dist = 0
    while not q.empty():
        dist, e = q.get()
        count += e
        if count > max_count:
            max_count = count
            max_dist = dist
    return max_dist

# Test the program with your input
with open('23.txt') as f:
    input_lines = f.readlines()
nanobots = parse_input(input_lines)
print(part1(nanobots))  # Part 1
print(part2(nanobots))  # Part 2