'''
Deux essais pour résoudre le jour 8 de 2017
'''
from collections import defaultdict
def parse_instruction(instruction):
    parts = instruction.split()
    reg, op, val, _, cond_reg, cond_op, cond_val = parts[0], parts[1], int(parts[2]), parts[3], parts[4], parts[5], int(parts[6])
    return reg, op, val, cond_reg, cond_op, cond_val

def execute_instruction(registers, instruction):
    reg, op, val, cond_reg, cond_op, cond_val = parse_instruction(instruction)
    if eval(f'registers["{cond_reg}"] {cond_op} {cond_val}'):
        if op == 'inc':
            registers[reg] += val
        else:
            registers[reg] -= val

def solve(input):
    registers = defaultdict(int)
    max_value_during_process = float('-inf')
    for instruction in input.split('\n'):
        execute_instruction(registers, instruction)
        max_value_during_process = max(max_value_during_process, max(registers.values()))
    return max(registers.values()), max_value_during_process

input = open('08.txt').read()

# Partie 1 et 2
print(solve(input.strip()))