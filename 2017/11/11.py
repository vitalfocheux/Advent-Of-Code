'''
Un essai pour résoudre le jour 11 de 2017
'''
def hex_distance(x, y, z):
    return (abs(x) + abs(y) + abs(z)) // 2

def solve(input):
    x = y = z = 0
    max_distance = 0
    for direction in input.split(','):
        if direction == 'n':
            y += 1
            z -= 1
        elif direction == 'ne':
            x += 1
            z -= 1
        elif direction == 'se':
            x += 1
            y -= 1
        elif direction == 's':
            y -= 1
            z += 1
        elif direction == 'sw':
            x -= 1
            z += 1
        elif direction == 'nw':
            x -= 1
            y += 1
        max_distance = max(max_distance, hex_distance(x, y, z))
    return hex_distance(x, y, z), max_distance

input = open('11.txt').read()

# Partie 1 et 2
print(solve(input.strip()))