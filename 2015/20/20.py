'''
Un essai pour résoudre le jour 20 de 2015
'''
def solve_part1(target):
    houses = [0] * (target // 10)
    for elf in range(1, target // 10):
        for house in range(elf, target // 10, elf):
            houses[house] += elf * 10
        if houses[elf] >= target:
            return elf

def solve_part2(target):
    houses = [0] * (target // 10)
    for elf in range(1, target // 10):
        for house in range(elf, min(elf*50, target // 10), elf):
            houses[house] += elf * 11
        if houses[elf] >= target:
            return elf

target = 36000000

# Part 1
print(solve_part1(target))

# Part 2
print(solve_part2(target))