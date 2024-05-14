'''
Cinq essais pour la partie 1
La partie 2 ne fonctionne pas
'''
import re

def parse_samples(samples):
    return [(list(map(int, re.findall(r'\d+', line))) for line in sample.splitlines()) for sample in samples.split('\n\n')]

def parse_program(program):
    return [list(map(int, re.findall(r'\d+', line))) for line in program.splitlines()]

def execute(opcode, registers, a, b, c):
    if opcode == 'addr': registers[c] = registers[a] + registers[b]
    elif opcode == 'addi': registers[c] = registers[a] + b
    elif opcode == 'mulr': registers[c] = registers[a] * registers[b]
    elif opcode == 'muli': registers[c] = registers[a] * b
    elif opcode == 'banr': registers[c] = registers[a] & registers[b]
    elif opcode == 'bani': registers[c] = registers[a] & b
    elif opcode == 'borr': registers[c] = registers[a] | registers[b]
    elif opcode == 'bori': registers[c] = registers[a] | b
    elif opcode == 'setr': registers[c] = registers[a]
    elif opcode == 'seti': registers[c] = a
    elif opcode == 'gtir': registers[c] = int(a > registers[b])
    elif opcode == 'gtri': registers[c] = int(registers[a] > b)
    elif opcode == 'gtrr': registers[c] = int(registers[a] > registers[b])
    elif opcode == 'eqir': registers[c] = int(a == registers[b])
    elif opcode == 'eqri': registers[c] = int(registers[a] == b)
    elif opcode == 'eqrr': registers[c] = int(registers[a] == registers[b])

def solve_part1(samples):
    opcodes = ['addr', 'addi', 'mulr', 'muli', 'banr', 'bani', 'borr', 'bori', 'setr', 'seti', 'gtir', 'gtri', 'gtrr', 'eqir', 'eqri', 'eqrr']
    count = 0
    for before, instruction, after in samples:
        opcode, a, b, c = instruction
        matches = 0
        for op in opcodes:
            registers = before[:]
            execute(op, registers, a, b, c)
            if registers == after:
                matches += 1
        if matches >= 3:
            count += 1
    return count

with open('16.txt') as f:
    content = f.read().split('\n\n\n\n')
    samples, program = content
    samples = parse_samples(samples)
    program = parse_program(program)
    print(solve_part1(samples))