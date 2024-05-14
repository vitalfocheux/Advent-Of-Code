'''
Un essai pour la partie 1
Dix essai pour la partie 2
'''
from collections import defaultdict, deque

def get_value(registers, arg):
    if arg.isalpha():
        return registers[arg]
    else:
        return int(arg)

def solve_part1(instructions):
    registers = defaultdict(int)
    last_sound = None
    pc = 0

    while 0 <= pc < len(instructions):
        op, *args = instructions[pc].split()

        if op == 'snd':
            last_sound = get_value(registers, args[0])
        elif op == 'set':
            registers[args[0]] = get_value(registers, args[1])
        elif op == 'add':
            registers[args[0]] += get_value(registers, args[1])
        elif op == 'mul':
            registers[args[0]] *= get_value(registers, args[1])
        elif op == 'mod':
            registers[args[0]] %= get_value(registers, args[1])
        elif op == 'rcv':
            if get_value(registers, args[0]) != 0:
                return last_sound
        elif op == 'jgz':
            if get_value(registers, args[0]) > 0:
                pc += get_value(registers, args[1])
                continue

        pc += 1

def solve_part2(instructions):
    registers = [defaultdict(int, {'p': i}) for i in range(2)]
    queues = [deque() for _ in range(2)]
    pcs = [0, 0]
    send_count = [0, 0]
    deadlock = [False, False]

    while not all(deadlock):
        for i in range(2):
            if not (0 <= pcs[i] < len(instructions)):
                deadlock[i] = True
                continue

            op, *args = instructions[pcs[i]].split()

            if op == 'snd':
                queues[1 - i].append(get_value(registers[i], args[0]))
                send_count[i] += 1
            elif op == 'set':
                registers[i][args[0]] = get_value(registers[i], args[1])
            elif op == 'add':
                registers[i][args[0]] += get_value(registers[i], args[1])
            elif op == 'mul':
                registers[i][args[0]] *= get_value(registers[i], args[1])
            elif op == 'mod':
                registers[i][args[0]] %= get_value(registers[i], args[1])
            elif op == 'rcv':
                if queues[i]:
                    registers[i][args[0]] = queues[i].popleft()
                    deadlock[i] = False
                else:
                    deadlock[i] = True
                    continue
            elif op == 'jgz':
                if get_value(registers[i], args[0]) > 0:
                    pcs[i] += get_value(registers[i], args[1])
                    continue

            pcs[i] += 1

    return send_count[1]

instructions = open('18.txt').read().splitlines()
print(solve_part1(instructions))  # Part 1
print(solve_part2(instructions))  # Part 2