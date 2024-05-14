'''
Un essai pour résoudre le jour 5 de l'année 2019
'''
def parse_input(input_lines):
    return list(map(int, input_lines[0].split(',')))

def run_program(program, input_value):
    program = program[:]
    i = 0
    output = None
    while program[i] != 99:
        opcode = program[i] % 100
        modes = program[i] // 100
        if opcode in [1, 2]:
            a = program[i+1] if modes % 10 == 1 else program[program[i+1]]
            b = program[i+2] if modes // 10 == 1 else program[program[i+2]]
            program[program[i+3]] = a + b if opcode == 1 else a * b
            i += 4
        elif opcode == 3:
            program[program[i+1]] = input_value
            i += 2
        elif opcode == 4:
            output = program[i+1] if modes % 10 == 1 else program[program[i+1]]
            i += 2
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
    return output

def part1(input_lines):
    program = parse_input(input_lines)
    return run_program(program, 1)

def part2(input_lines):
    program = parse_input(input_lines)
    return run_program(program, 5)

# Test the program with your input
with open('05.txt') as f:
    input_lines = f.readlines()
print(part1(input_lines))  # Part 1
print(part2(input_lines))  # Part 2