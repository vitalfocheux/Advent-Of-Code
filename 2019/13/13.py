'''
Un essai pour la partie 1
La partie 2 ne fonctionne pas
'''
from collections import defaultdict

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
            if inputs:
                program[out(1)] = inputs.pop(0)
            else:
                program[out(1)] = yield
            i += 2
        elif opcode == 4:
            yield arg(1)
            i += 2
        elif opcode == 5:
            i = arg(2) if arg(1) != 0 else i + 3
        elif opcode == 6:
            i = arg(2) if arg(1) == 0 else i + 3
        elif opcode == 7:
            if arg(1) is not None and arg(2) is not None:
                program[out(3)] = int(arg(1) < arg(2))
            else:
                raise ValueError(f"Unexpected None value at opcode 7: arg(1)={arg(1)}, arg(2)={arg(2)}")
            i += 4
        elif opcode == 8:
            program[out(3)] = int(arg(1) == arg(2))
            i += 4
        elif opcode == 9:
            relative_base += arg(1)
            i += 2

def run_game(program, free_play=False):
    if free_play: program[0] = 2
    outputs = run_program(program, [])
    screen = defaultdict(int)
    score = 0
    paddle = None
    ball = None
    while True:
        try:
            x = next(outputs)
            y = next(outputs)
            tile = next(outputs)
            if x == -1 and y == 0:
                score = tile
            else:
                screen[(x, y)] = tile
                if tile == 3: paddle = x
                if tile == 4: ball = x
            if free_play and ball is not None and paddle is not None:
                direction = 0 if ball == paddle else 1 if ball > paddle else -1
                outputs.send(direction)
        except StopIteration:
            break
    return screen, score

program = list(map(int, open('13.txt').read().split(',')))

# Part 1
screen, _ = run_game(program[:])
print(list(screen.values()).count(2))

# Part 2
_, score = run_game(program[:], True)
print(score)