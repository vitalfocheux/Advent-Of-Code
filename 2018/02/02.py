'''
Un essai pour résoudre le jour 2 de l'année 2018
'''
from collections import Counter

def solve_part1(ids):
    twos = threes = 0
    for id in ids:
        counts = Counter(id).values()
        twos += 2 in counts
        threes += 3 in counts
    return twos * threes

def solve_part2(ids):
    for id1 in ids:
        for id2 in ids:
            diff = [c1 != c2 for c1, c2 in zip(id1, id2)]
            if sum(diff) == 1:
                return ''.join(c1 for c1, c2, d in zip(id1, id2, diff) if not d)

# Assuming ids is a list of strings read from the input file
with open('02.txt', 'r') as file:
    ids = [line.strip() for line in file]

print(solve_part1(ids))  # Part 1
print(solve_part2(ids))  # Part 2