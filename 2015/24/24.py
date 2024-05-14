'''
Deux essais pour résoudre le jour 24 de l'AOC 2015
'''

from itertools import combinations
from functools import reduce

def read_weights(filename):
    with open(filename, 'r') as file:
        return [int(line.strip()) for line in file]

def find_min_product(weights, num_groups):
    group_weight = sum(weights) // num_groups
    for i in range(len(weights)):
        valid_groups = [comb for comb in combinations(weights, i) if sum(comb) == group_weight]
        if valid_groups:
            return min([reduce(lambda x, y: x * y, group) for group in valid_groups])

def solve_part1(weights):
    return find_min_product(weights, 3)

def solve_part2(weights):
    return find_min_product(weights, 4)

# Read weights from file
weights = read_weights('24.txt')

# Part 1
print(solve_part1(weights))

# Part 2
print(solve_part2(weights))