'''
Un essaie pour résoudre le jour 19 de 2015
'''
import re

def read_data(file_path):
    with open(file_path, 'r') as file:
        lines = file.read().splitlines()
        molecule = lines[-1]
        transformations = [tuple(re.findall(r'(\w+) => (\w+)', line)[0]) for line in lines[:-2]]
    return molecule, transformations

def solve_part1(molecule, transformations):
    results = set()
    for a, b in transformations:
        for i in range(len(molecule)):
            if molecule[i:i+len(a)] == a:
                results.add(molecule[:i] + b + molecule[i+len(a):])
    return len(results)

def solve_part2(molecule, transformations):
    target = molecule
    steps = 0
    while target != 'e':
        for a, b in transformations:
            if b in target:
                target = target.replace(b, a, 1)
                steps += 1
    return steps

molecule, transformations = read_data('19.txt')

# Part 1
print(solve_part1(molecule, transformations))

# Part 2
print(solve_part2(molecule, transformations))