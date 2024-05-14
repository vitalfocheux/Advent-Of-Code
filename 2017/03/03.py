'''
Cinq essais pour résoudre le jour 3 de l'Avent of Code 2017
'''
import itertools

def spiral():
    x = y = 0
    yield x, y
    for dist in itertools.count(1, 2):
        for _ in range(dist): x += 1; yield x, y
        for _ in range(dist): y -= 1; yield x, y
        for _ in range(dist + 1): x -= 1; yield x, y
        for _ in range(dist + 1): y += 1; yield x, y

def solve_part1(input):
    for i, (x, y) in enumerate(spiral(), 1):
        if i == input:
            return abs(x) + abs(y)

def solve_part2(input):
    values = {(0, 0): 1}
    for x, y in spiral():
        if (x, y) == (0, 0):
            continue
        values[(x, y)] = sum(values.get((nx, ny), 0) for nx, ny in ((x + dx, y + dy) for dx in (-1, 0, 1) for dy in (-1, 0, 1)))
        if values[(x, y)] > input:
            return values[(x, y)]

input = 277678

# Partie 1
print(solve_part1(input))

# Partie 2
print(solve_part2(input))