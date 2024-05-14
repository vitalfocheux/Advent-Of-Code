'''
Un essai pour la partie 1
La partie 2 ne fonctionne pas
'''
def parse_input(input):
    ip_reg = int(input[0].split()[1])
    program = [line.split() for line in input[1:]]
    for instruction in program:
        instruction[1:] = map(int, instruction[1:])
    return ip_reg, program

def execute(instruction, registers, opcodes):
    op, a, b, c = instruction
    registers[c] = opcodes[op](registers, a, b)
    return registers

def solve(input, part2=False):
    ip_reg, program = parse_input(input)
    registers = [0]*6
    if part2:
        registers[0] = 1
    opcodes = {
        'addr': lambda r, a, b: r[a] + r[b],
        'addi': lambda r, a, b: r[a] + b,
        'mulr': lambda r, a, b: r[a] * r[b],
        'muli': lambda r, a, b: r[a] * b,
        'banr': lambda r, a, b: r[a] & r[b],
        'bani': lambda r, a, b: r[a] & b,
        'borr': lambda r, a, b: r[a] | r[b],
        'bori': lambda r, a, b: r[a] | b,
        'setr': lambda r, a, b: r[a],
        'seti': lambda r, a, b: a,
        'gtir': lambda r, a, b: int(a > r[b]),
        'gtri': lambda r, a, b: int(r[a] > b),
        'gtrr': lambda r, a, b: int(r[a] > r[b]),
        'eqir': lambda r, a, b: int(a == r[b]),
        'eqri': lambda r, a, b: int(r[a] == b),
        'eqrr': lambda r, a, b: int(r[a] == r[b]),
    }
    while 0 <= registers[ip_reg] < len(program):
        instruction = program[registers[ip_reg]]
        registers = execute(instruction, registers, opcodes)
        registers[ip_reg] += 1
    return registers[0]

with open('19.txt') as f:
    input = f.read().splitlines()
    print(solve(input))  # Part 1
    print(solve(input, part2=True))  # Part 2