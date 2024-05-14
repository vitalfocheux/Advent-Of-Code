'''
Un essai pour résoudre le jour 1 de l'année 2019
'''
def parse_input(input_lines):
    return [int(line) for line in input_lines]

def fuel_required(mass):
    return mass // 3 - 2

def total_fuel_required(mass):
    total = 0
    while (fuel := fuel_required(mass)) > 0:
        total += fuel
        mass = fuel
    return total

def part1(input_lines):
    masses = parse_input(input_lines)
    return sum(fuel_required(mass) for mass in masses)

def part2(input_lines):
    masses = parse_input(input_lines)
    return sum(total_fuel_required(mass) for mass in masses)

# Test the program with your input
with open('01.txt') as f:
    input_lines = f.readlines()
print(part1(input_lines))  # Part 1
print(part2(input_lines))  # Part 2