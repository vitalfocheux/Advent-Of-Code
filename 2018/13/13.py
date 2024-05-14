'''
Un essai pour la partie 1
Deux essais pour la partie 2
'''
import copy

def parse_input(input):
    grid = [list(line) for line in input.splitlines()]
    carts = []
    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            if cell in '^v<>':
                carts.append(((x, y), cell, 0))
                grid[y][x] = '|' if cell in '^v' else '-'
    return grid, carts

def move_cart(grid, cart):
    (x, y), direction, intersection = cart
    if direction == '^':
        y -= 1
    elif direction == 'v':
        y += 1
    elif direction == '<':
        x -= 1
    elif direction == '>':
        x += 1
    cell = grid[y][x]
    if cell == '/':
        direction = '^' if direction == '>' else '>' if direction == '^' else '<' if direction == 'v' else 'v'
    elif cell == '\\':
        direction = 'v' if direction == '>' else '<' if direction == '^' else '>' if direction == 'v' else '^'
    elif cell == '+':
        direction = ('<' if direction == '^' else '^' if direction == '>' else '>' if direction == 'v' else 'v') if intersection == 0 else \
                    ('>' if direction == '^' else 'v' if direction == '>' else '<' if direction == 'v' else '^') if intersection == 2 else direction
        intersection = (intersection + 1) % 3
    return ((x, y), direction, intersection)

def solve_part1(input):
    grid, carts = parse_input(input)
    while True:
        carts.sort()
        for i, cart in enumerate(carts):
            carts[i] = move_cart(grid, cart)
            if any(carts[i][0] == other_cart[0] for other_cart in carts[:i] + carts[i+1:]):
                return carts[i][0]

def solve_part2(input):
    grid, carts = parse_input(input)
    while len(carts) > 1:
        crashed = set()
        for cart in sorted(carts, key=lambda x: x[0]):
            if cart not in crashed:
                carts.remove(cart)
                cart = move_cart(grid, cart)
                if any(cart[0] == other_cart[0] for other_cart in carts):
                    crashed.update([c for c in carts if c[0] == cart[0]])
                    carts = [c for c in carts if c[0] != cart[0]]
                else:
                    carts.append(cart)
    return carts[0][0]

input = open('13.txt').read()
print(solve_part1(input))  # solution for part 1
print(solve_part2(input))  # solution for part 2