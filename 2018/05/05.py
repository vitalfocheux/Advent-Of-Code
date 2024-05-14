'''
Un essai pour résoudre le jour 5 de l'année 2018
'''
def react(polymer):
    stack = []
    for unit in polymer:
        if stack and stack[-1] != unit and stack[-1].lower() == unit.lower():
            stack.pop()
        else:
            stack.append(unit)
    return ''.join(stack)

def solve_part1(polymer):
    return len(react(polymer))

def solve_part2(polymer):
    return min(len(react(polymer.replace(unit, '').replace(unit.upper(), ''))) for unit in set(polymer.lower()))

# Assuming polymer is a string read from the input file
with open('05.txt', 'r') as file:
    polymer = file.read().strip()

print(solve_part1(polymer))  # Part 1
print(solve_part2(polymer))  # Part 2