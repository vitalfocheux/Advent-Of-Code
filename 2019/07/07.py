'''
Un essai pour la partie 1
La partie 2 ne fonctionne pas
'''
from itertools import permutations

def parse_input(input_lines):
    return list(map(int, input_lines[0].split(',')))

def run_program(program, inputs, i=0):
    program = program[:]
    input_index = 0
    while program[i] != 99:
        opcode = program[i] % 100
        modes = program[i] // 100
        if opcode in [1, 2]:
            a = program[i+1] if modes % 10 == 1 else program[program[i+1]]
            b = program[i+2] if modes // 10 == 1 else program[program[i+2]]
            program[program[i+3]] = a + b if opcode == 1 else a * b
            i += 4
        elif opcode == 3:
            if input_index < len(inputs):
                program[program[i+1]] = inputs[input_index]
                input_index += 1
            i += 2
        elif opcode == 4:
            return program[i+1] if modes % 10 == 1 else program[program[i+1]], program, i + 2
        elif opcode in [5, 6]:
            a = program[i+1] if modes % 10 == 1 else program[program[i+1]]
            b = program[i+2] if modes // 10 == 1 else program[program[i+2]]
            if (a != 0 and opcode == 5) or (a == 0 and opcode == 6):
                i = b
            else:
                i += 3
        elif opcode in [7, 8]:
            a = program[i+1] if modes % 10 == 1 else program[program[i+1]]
            b = program[i+2] if modes // 10 == 1 else program[program[i+2]]
            program[program[i+3]] = int((a < b and opcode == 7) or (a == b and opcode == 8))
            i += 4
    return None, program, i

def run_amplifiers(program, phases):
    signal = 0
    for phase in phases:
        signal, _, _ = run_program(program, [phase, signal])
    return signal

def part1(input_lines):
    program = parse_input(input_lines)
    return max(run_amplifiers(program, phases) for phases in permutations(range(5)))

def run_amplifiers_feedback(program, phases):
    programs = [program[:] for _ in phases]
    indices = [0 for _ in phases]
    signals = list(phases)
    signals[0] = 0
    i = 0
    while True:
        output, programs[i], indices[i] = run_program(programs[i], [signals[i]], indices[i])
        if output is None:
            if i == 0:
                return signals[0]
        else:
            signals[(i+1)%5] = output
        i = (i + 1) % 5

def part2(input_lines):
    program = parse_input(input_lines)
    return max(run_amplifiers_feedback(program, phases) for phases in permutations(range(5, 10)))

# Test the program with your input
with open('07.txt') as f:
    input_lines = f.readlines()
print(part1(input_lines))  # Part 1
print(part2(input_lines))  # Part 2