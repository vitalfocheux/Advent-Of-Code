'''
Un essai pour la partie 1
La partie 2 ne fonctionne pas
'''
from collections import defaultdict, deque
import re

def parse_instructions(instructions):
    dependencies = defaultdict(set)
    steps = set()
    for instruction in instructions:
        step, dependency = re.match(r'Step (.) .* step (.)', instruction).groups()
        dependencies[dependency].add(step)
        steps.add(step)
        steps.add(dependency)
    return steps, dependencies

def solve_part1(steps, dependencies):
    order = ''
    while steps:
        available = sorted(step for step in steps if not dependencies[step])
        step = available[0]
        order += step
        steps.remove(step)
        for dependency in dependencies.values():
            dependency.discard(step)
    return order

def solve_part2(steps, dependencies, workers=5, base_time=60):
    time = 0
    tasks = [None] * workers
    while steps or any(task is not None for task in tasks):
        for i in range(workers):
            if tasks[i] is not None and tasks[i][1] <= time:
                for dependency in dependencies.values():
                    dependency.discard(tasks[i][0])
                tasks[i] = None
        available = sorted(step for step in steps if not dependencies[step])
        for i in range(workers):
            if tasks[i] is None and available:
                step = available.pop(0)
                tasks[i] = (step, time + base_time + ord(step) - ord('A') + 1)
                steps.remove(step)
        if any(task is not None for task in tasks):
            time = min(task[1] for task in tasks if task is not None)
        else:
            break
    return time if tasks else 0

# Assuming instructions is a list of strings read from the input file
with open('07.txt', 'r') as file:
    instructions = [line.strip() for line in file]

steps, dependencies = parse_instructions(instructions)
print(solve_part1(steps.copy(), dependencies.copy()))  # Part 1
print(solve_part2(steps, dependencies))  # Part 2