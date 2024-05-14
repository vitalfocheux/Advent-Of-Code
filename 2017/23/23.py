'''
Un essai pour la partie 1
La partie 2 ne fonctionne pas
'''
def parse_instructions(input):
    return [line.split() for line in input.splitlines()]

def execute_instructions(instructions, part2=False):
    registers = {chr(97 + i): 0 for i in range(8)}
    if part2:
        registers['a'] = 1
    i = 0
    mul_count = 0
    while 0 <= i < len(instructions):
        instr = instructions[i]
        op, x, y = instr[0], instr[1], instr[-1]
        y_val = registers[y] if y in registers else int(y)
        if op == 'set':
            registers[x] = y_val
        elif op == 'sub':
            registers[x] -= y_val
        elif op == 'mul':
            registers[x] *= y_val
            mul_count += 1
        elif op == 'jnz' and (registers[x] if x in registers else int(x)) != 0:
            i += y_val - 1
        i += 1
    return mul_count if not part2 else registers['h']

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def parse_input(input):
    lines = input.split('\n')
    b = int(lines[0].split(' ')[2])
    c = int(lines[4].split(' ')[2])
    interval = int(lines[30].split(' ')[2])
    return b * 100 + 100000, c * 100 + 100000, interval

def execute_instructions_optimized(input):
    lines = input.strip().split('\n')
    a = 1
    b = 0
    c = 0
    d = 0
    e = 0
    f = 0
    g = 0
    h = 0
    b = 93
    c = b
    if a != 0:
        b *= 100
        b += 100000
        c = b
        c += 17000
    while True:
        f = 1
        d = 2
        e = 2
        for d in range(2, b):
            if b % d == 0:
                f = 0
                break
        if f == 0:
            h += 1
        g = b - c
        if g == 0:
            return h
        b += 17

input = open('23.txt').read()
instructions = parse_instructions(input)
print(execute_instructions(instructions))  # Part 1
print(execute_instructions_optimized(input))  # Part 2