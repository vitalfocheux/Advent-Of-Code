'''
Un essai pour résoudre le jour 1 de l'année 2018
'''
def solve_part1(changes):
    return sum(changes)

def solve_part2(changes):
    frequency = 0
    seen = {frequency}
    while True:
        for change in changes:
            frequency += change
            if frequency in seen:
                return frequency
            seen.add(frequency)

# Assuming changes is a list of integers read from the input file
with open('01.txt', 'r') as file:
    changes = [int(line.strip()) for line in file]

print(solve_part1(changes))  # Part 1
print(solve_part2(changes))  # Part 2