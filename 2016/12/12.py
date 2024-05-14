'''
Un essai pour résoudre le problème 12 de Advent of Code 2016
'''
def read_instructions(file_path):
    with open(file_path, 'r') as file:
        return [line.strip().split() for line in file]

def execute_instructions(instructions, registers):
    i = 0
    while i < len(instructions):
        inst = instructions[i]
        if inst[0] == 'cpy':
            if inst[1].isdigit():
                registers[inst[2]] = int(inst[1])
            else:
                registers[inst[2]] = registers[inst[1]]
        elif inst[0] == 'inc':
            registers[inst[1]] += 1
        elif inst[0] == 'dec':
            registers[inst[1]] -= 1
        elif inst[0] == 'jnz':
            if (inst[1].isdigit() and inst[1] != '0') or registers[inst[1]] != 0:
                i += int(inst[2]) - 1
        i += 1
    return registers

instructions = read_instructions('12.txt')

# Part 1
registers = {'a': 0, 'b': 0, 'c': 0, 'd': 0}
registers = execute_instructions(instructions, registers)
print(registers['a'])

# Part 2
registers = {'a': 0, 'b': 0, 'c': 1, 'd': 0}
registers = execute_instructions(instructions, registers)
print(registers['a'])