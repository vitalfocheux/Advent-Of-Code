'''
Un essaie pour résoudre le jour 3 de l'année 2018
'''
import re
from collections import defaultdict

def solve_part1(claims):
    fabric = defaultdict(int)
    for _, left, top, width, height in claims:
        for x in range(left, left + width):
            for y in range(top, top + height):
                fabric[x, y] += 1
    return sum(value >= 2 for value in fabric.values())

def solve_part2(claims):
    fabric = defaultdict(list)
    for id, left, top, width, height in claims:
        for x in range(left, left + width):
            for y in range(top, top + height):
                fabric[x, y].append(id)
    overlapping = set(id for ids in fabric.values() if len(ids) > 1 for id in ids)
    for id, _, _, _, _ in claims:
        if id not in overlapping:
            return id

# Assuming claims is a list of tuples read from the input file
with open('03.txt', 'r') as file:
    claims = [tuple(map(int, re.findall(r'\d+', line))) for line in file]

print(solve_part1(claims))  # Part 1
print(solve_part2(claims))  # Part 2