'''
Un essai pour résoudre le jour 17 de 2015
'''
from itertools import combinations

def read_containers(file_path):
    with open(file_path, 'r') as file:
        return [int(line.strip()) for line in file]

def find_combinations(containers, total):
    return [combo for i in range(len(containers)) for combo in combinations(containers, i) if sum(combo) == total]

def solve_part1(containers):
    return len(find_combinations(containers, 150))

def solve_part2(containers):
    combinations = find_combinations(containers, 150)
    min_length = min(len(combo) for combo in combinations)
    return len([combo for combo in combinations if len(combo) == min_length])

containers = read_containers('17.txt')

# Part 1
print(solve_part1(containers))

# Part 2
print(solve_part2(containers))