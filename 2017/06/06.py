'''
Un essai pour résoudre le jour 6 de l'Avent of Code 2017
'''
def redistribute(banks):
    max_blocks = max(banks)
    index = banks.index(max_blocks)
    banks[index] = 0
    while max_blocks:
        index = (index + 1) % len(banks)
        banks[index] += 1
        max_blocks -= 1

def solve_part1(input):
    banks = list(map(int, input.split()))
    seen = set()
    while tuple(banks) not in seen:
        seen.add(tuple(banks))
        redistribute(banks)
    return len(seen)

def solve_part2(input):
    banks = list(map(int, input.split()))
    seen = {}
    while tuple(banks) not in seen:
        seen[tuple(banks)] = len(seen)
        redistribute(banks)
    return len(seen) - seen[tuple(banks)]

input = open('06.txt').read().strip()

# Partie 1
print(solve_part1(input))

# Partie 2
print(solve_part2(input))