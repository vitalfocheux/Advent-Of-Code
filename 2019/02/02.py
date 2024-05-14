'''
Un essai pour résoudre le jour 2 de l'année 2019
'''
def parse_input(input_lines):
    return list(map(int, input_lines[0].split(',')))

def run_program(memory, noun, verb):
    memory[1] = noun
    memory[2] = verb
    pc = 0
    while memory[pc] != 99:
        if memory[pc] == 1:
            memory[memory[pc+3]] = memory[memory[pc+1]] + memory[memory[pc+2]]
        elif memory[pc] == 2:
            memory[memory[pc+3]] = memory[memory[pc+1]] * memory[memory[pc+2]]
        pc += 4
    return memory[0]

def part1(input_lines):
    memory = parse_input(input_lines)
    return run_program(memory, 12, 2)

def part2(input_lines):
    memory = parse_input(input_lines)
    for noun in range(100):
        for verb in range(100):
            if run_program(memory.copy(), noun, verb) == 19690720:
                return 100 * noun + verb

# Test the program with your input
with open('02.txt') as f:
    input_lines = f.readlines()
print(part1(input_lines))  # Part 1
print(part2(input_lines))  # Part 2