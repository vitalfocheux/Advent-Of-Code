'''
Un essai pour résoudre le jour 1 de l'année 2015
'''
def read_instructions(file_path):
    with open(file_path, 'r') as file:
        return file.read().strip()

def part1(instructions):
    return instructions.count("(") - instructions.count(")")

def part2(instructions):
    floor = 0
    for i, instruction in enumerate(instructions):
        if instruction == "(":
            floor += 1
        else:
            floor -= 1
        if floor == -1:
            return i + 1

instructions = read_instructions("01.txt")

# Part 1
print(part1(instructions))

# Part 2
print(part2(instructions))