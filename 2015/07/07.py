'''
Deux essais pour résoudre le jour 7 de l'année 2015
'''

import re

def read_instructions(file_path):
    with open(file_path, 'r') as file:
        return {right: left for left, right in [re.split(' -> ', line.strip()) for line in file]}

def evaluate(wire, instructions, cache):
    if wire.isdigit():
        return int(wire)
    if wire not in cache:
        if 'AND' in instructions[wire]:
            a, _, b = instructions[wire].split()
            cache[wire] = evaluate(a, instructions, cache) & evaluate(b, instructions, cache)
        elif 'OR' in instructions[wire]:
            a, _, b = instructions[wire].split()
            cache[wire] = evaluate(a, instructions, cache) | evaluate(b, instructions, cache)
        elif 'NOT' in instructions[wire]:
            _, a = instructions[wire].split()
            cache[wire] = ~evaluate(a, instructions, cache) & 0xffff
        elif 'LSHIFT' in instructions[wire]:
            a, _, b = instructions[wire].split()
            cache[wire] = evaluate(a, instructions, cache) << evaluate(b, instructions, cache)
        elif 'RSHIFT' in instructions[wire]:
            a, _, b = instructions[wire].split()
            cache[wire] = evaluate(a, instructions, cache) >> evaluate(b, instructions, cache)
        else:
            cache[wire] = evaluate(instructions[wire], instructions, cache)
    return cache[wire]

instructions = read_instructions('07.txt')

# Part 1
print(evaluate('a', instructions, {}))

# Part 2
instructions['b'] = str(evaluate('a', instructions, {}))
print(evaluate('a', instructions, {}))