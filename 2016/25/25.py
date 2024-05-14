def read_input(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file.readlines()]

def execute_instructions(instructions):
    registers = {'a': 0, 'b': 0, 'c': 0, 'd': 0}
    i = 0
    while i < len(instructions):
        parts = instructions[i].split()
        if parts[0] == 'cpy':
            if parts[1].isdigit():
                registers[parts[2]] = int(parts[1])
            else:
                registers[parts[2]] = registers[parts[1]]
        elif parts[0] == 'inc':
            registers[parts[1]] += 1
        elif parts[0] == 'dec':
            registers[parts[1]] -= 1
        elif parts[0] == 'jnz':
            if ((parts[1].isdigit() and parts[1] != '0') or (parts[1] in registers and registers[parts[1]] != 0)) and int(parts[2]) > 0:
                i += int(parts[2]) - 1
        i += 1
    return registers

def solve_part1(instructions):
    registers = execute_instructions(instructions)
    return registers['a']

def solve_part2(instructions):
    instructions = ['cpy 1 c'] + instructions
    registers = execute_instructions(instructions)
    return registers['a']

instructions = read_input('25.txt')

# Part 1
print(solve_part1(instructions))

# Part 2
print(solve_part2(instructions))