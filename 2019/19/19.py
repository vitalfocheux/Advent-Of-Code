'''
Un essai pour la partie 1
'''
from itertools import count

def run_intcode(program, inputs):
    program = program + [0] * 10000
    pc = rb = 0
    while program[pc] != 99:
        opcode = program[pc] % 100
        modes = program[pc] // 100
        def arg(n):
            if modes // 10 ** (n - 1) % 10 == 2:
                return program[rb + program[pc + n]]
            elif modes // 10 ** (n - 1) % 10 == 1:
                return program[pc + n]
            else:
                return program[program[pc + n]]
        def out(n):
            if modes // 10 ** (n - 1) % 10 == 2:
                return rb + program[pc + n]
            else:
                return program[pc + n]
        if opcode == 1:
            program[out(3)] = arg(1) + arg(2)
            pc += 4
        elif opcode == 2:
            program[out(3)] = arg(1) * arg(2)
            pc += 4
        elif opcode == 3:
            program[out(1)] = inputs.pop(0)
            pc += 2
        elif opcode == 4:
            return arg(1)
            pc += 2
        elif opcode == 5:
            pc = arg(2) if arg(1) != 0 else pc + 3
        elif opcode == 6:
            pc = arg(2) if arg(1) == 0 else pc + 3
        elif opcode == 7:
            program[out(3)] = int(arg(1) < arg(2))
            pc += 4
        elif opcode == 8:
            program[out(3)] = int(arg(1) == arg(2))
            pc += 4
        elif opcode == 9:
            rb += arg(1)
            pc += 2

def part1(program):
    return sum(run_intcode(program[:], [x, y]) for y in range(50) for x in range(50))

def part2(program):
    x = y = 0
    for y in count(start=99):
        while not run_intcode(program[:], [x, y]):
            x += 1
        if y > 99 and run_intcode(program[:], [x - 99, y - 99]):
            return (x - 99) * 10000 + (y - 99)

program = list(map(int, open('19.txt').read().split(',')))
print("Part 1:", part1(program))
print("Part 2:", part2(program))