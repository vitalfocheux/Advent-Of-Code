'''
Un essai pour résoudre le jour 3 de l'année 2015
'''
def read_instructions(file_path):
    with open(file_path, 'r') as file:
        return file.read().strip()

def part1(instructions):
    houses = {(0, 0)}
    x, y = 0, 0
    for instruction in instructions:
        if instruction == '^':
            y += 1
        elif instruction == 'v':
            y -= 1
        elif instruction == '>':
            x += 1
        elif instruction == '<':
            x -= 1
        houses.add((x, y))
    return len(houses)

def part2(instructions):
    houses = {(0, 0)}
    santas = [(0, 0), (0, 0)]
    for i, instruction in enumerate(instructions):
        x, y = santas[i % 2]
        if instruction == '^':
            y += 1
        elif instruction == 'v':
            y -= 1
        elif instruction == '>':
            x += 1
        elif instruction == '<':
            x -= 1
        santas[i % 2] = (x, y)
        houses.add((x, y))
    return len(houses)

instructions = read_instructions('03.txt')

# Part 1
print(part1(instructions))

# Part 2
print(part2(instructions))