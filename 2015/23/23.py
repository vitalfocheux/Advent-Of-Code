'''
Un essai pour résoudre le problème 23 de l'AOC 2015
'''
def read_instructions(filename):
    with open(filename, 'r') as file:
        return [line.strip() for line in file]

def execute_instructions(instructions, registers):
    i = 0
    while i < len(instructions):
        instruction = instructions[i].split()
        if instruction[0] == 'hlf':
            registers[instruction[1]] //= 2
        elif instruction[0] == 'tpl':
            registers[instruction[1]] *= 3
        elif instruction[0] == 'inc':
            registers[instruction[1]] += 1
        elif instruction[0] == 'jmp':
            i += int(instruction[1])
            continue
        elif instruction[0] == 'jie':
            if registers[instruction[1].strip(',')] % 2 == 0:
                i += int(instruction[2])
                continue
        elif instruction[0] == 'jio':
            if registers[instruction[1].strip(',')] == 1:
                i += int(instruction[2])
                continue
        i += 1
    return registers['b']

def solve_part1(instructions):
    registers = {'a': 0, 'b': 0}
    return execute_instructions(instructions, registers)

def solve_part2(instructions):
    registers = {'a': 1, 'b': 0}
    return execute_instructions(instructions, registers)

# Read instructions from file
instructions = read_instructions('23.txt')

# Part 1
print(solve_part1(instructions))

# Part 2
print(solve_part2(instructions))