'''
Un essai pour résoudre le jour 5 de l'Avent of Code 2017
'''
def solve_part1(input):
    instructions = list(map(int, input.split('\n')))
    index = steps = 0
    while 0 <= index < len(instructions):
        jump = instructions[index]
        instructions[index] += 1
        index += jump
        steps += 1
    return steps

def solve_part2(input):
    instructions = list(map(int, input.split('\n')))
    index = steps = 0
    while 0 <= index < len(instructions):
        jump = instructions[index]
        if jump >= 3:
            instructions[index] -= 1
        else:
            instructions[index] += 1
        index += jump
        steps += 1
    return steps

input = open('05.txt').read().strip()

# Partie 1
print(solve_part1(input))

# Partie 2
print(solve_part2(input))