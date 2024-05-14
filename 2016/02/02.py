'''
Un essai pour résoudre le problème du jour 2.
'''

def read_instructions(file_path):
    with open(file_path, 'r') as file:
        return file.read().splitlines()

def calculate_code(instructions, keypad, start):
    x, y = start
    code = ''
    for instruction in instructions:
        for move in instruction:
            dx, dy = 0, 0
            if move == 'U':
                dx, dy = -1, 0
            elif move == 'D':
                dx, dy = 1, 0
            elif move == 'L':
                dx, dy = 0, -1
            elif move == 'R':
                dx, dy = 0, 1
            if 0 <= x + dx < len(keypad) and 0 <= y + dy < len(keypad[0]) and keypad[x + dx][y + dy] != ' ':
                x, y = x + dx, y + dy
        code += keypad[x][y]
    return code

instructions = read_instructions('02.txt')

# Part 1
keypad1 = [
    ['1', '2', '3'],
    ['4', '5', '6'],
    ['7', '8', '9']
]
start1 = (1, 1)
print(calculate_code(instructions, keypad1, start1))

# Part 2
keypad2 = [
    [' ', ' ', '1', ' ', ' '],
    [' ', '2', '3', '4', ' '],
    ['5', '6', '7', '8', '9'],
    [' ', 'A', 'B', 'C', ' '],
    [' ', ' ', 'D', ' ', ' ']
]
start2 = (2, 0)
print(calculate_code(instructions, keypad2, start2))