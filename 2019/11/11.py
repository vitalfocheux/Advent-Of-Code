'''
Deux essais pour résoudre le jour 11 de l'année 2019 du site Advent of Code
'''
from collections import defaultdict
from itertools import cycle

def run_program(program, inputs):
    program = program + [0]*10000  # Extend program with extra memory
    i = 0
    relative_base = 0
    while program[i] != 99:
        opcode = program[i] % 100
        modes = [(program[i] // 10**e) % 10 for e in range(2,5)]
        def arg(n):
            if modes[n-1] == 0: return program[program[i+n]]
            if modes[n-1] == 1: return program[i+n]
            if modes[n-1] == 2: return program[program[i+n]+relative_base]
        def out(n):
            if modes[n-1] == 0: return program[i+n]
            if modes[n-1] == 2: return program[i+n]+relative_base
        if opcode == 1:
            program[out(3)] = arg(1) + arg(2)
            i += 4
        elif opcode == 2:
            program[out(3)] = arg(1) * arg(2)
            i += 4
        elif opcode == 3:
            program[out(1)] = inputs.pop(0)
            i += 2
        elif opcode == 4:
            yield arg(1)
            i += 2
        elif opcode == 5:
            i = arg(2) if arg(1) != 0 else i + 3
        elif opcode == 6:
            i = arg(2) if arg(1) == 0 else i + 3
        elif opcode == 7:
            program[out(3)] = int(arg(1) < arg(2))
            i += 4
        elif opcode == 8:
            program[out(3)] = int(arg(1) == arg(2))
            i += 4
        elif opcode == 9:
            relative_base += arg(1)
            i += 2

def run_robot(program, start_color):
    panels = defaultdict(int)
    panels[(0, 0)] = start_color
    x, y = 0, 0
    dx, dy = 0, -1
    inputs = [panels[(x, y)]]
    outputs = run_program(program, inputs)
    while True:
        try:
            color = next(outputs)
            turn = next(outputs)
        except StopIteration:
            break
        panels[(x, y)] = color
        if turn == 0: dx, dy = dy, -dx
        else: dx, dy = -dy, dx
        x, y = x + dx, y + dy
        inputs.append(panels[(x, y)])
    return panels

program = list(map(int, open('11.txt').read().split(',')))

# Part 1
panels = run_robot(program[:], 0)
print(len(panels))

# Part 2
panels = run_robot(program[:], 1)
for y in range(6):
    for x in range(40):
        print('#' if panels[(x, y)] else ' ', end='')
    print()