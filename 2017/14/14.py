'''
Un essai pour résoudre le jour 14 de 2017
'''
from functools import reduce
from operator import xor
def knot_hash(input):
    numbers = list(range(256))
    lengths = [ord(c) for c in input] + [17, 31, 73, 47, 23]
    current_position = skip_size = 0
    for _ in range(64):
        numbers, current_position, skip_size = knot_hash_round(numbers, lengths, current_position, skip_size)
    dense_hash = [reduce(xor, numbers[i*16:(i+1)*16]) for i in range(16)]
    return ''.join(f'{num:02x}' for num in dense_hash)

def knot_hash_round(numbers, lengths, current_position=0, skip_size=0):
    for length in lengths:
        if current_position + length <= len(numbers):
            numbers[current_position:current_position + length] = reversed(numbers[current_position:current_position + length])
        else:
            temp = (numbers[current_position:] + numbers[:(current_position + length) % len(numbers)])[::-1]
            numbers[current_position:] = temp[:len(numbers) - current_position]
            numbers[:(current_position + length) % len(numbers)] = temp[len(numbers) - current_position:]
        current_position = (current_position + length + skip_size) % len(numbers)
        skip_size += 1
    return numbers, current_position, skip_size

def solve(input):
    grid = []
    for i in range(128):
        row_hash = knot_hash(f'{input}-{i}')
        row_bin = ''.join(f'{int(c, 16):04b}' for c in row_hash)
        grid.append(list(map(int, row_bin)))
    used_squares = sum(sum(row) for row in grid)
    regions = 0
    for i in range(128):
        for j in range(128):
            if grid[i][j] == 1:
                dfs(grid, i, j)
                regions += 1
    return used_squares, regions

def dfs(grid, i, j):
    if i < 0 or i >= 128 or j < 0 or j >= 128 or grid[i][j] == 0:
        return
    grid[i][j] = 0
    dfs(grid, i-1, j)
    dfs(grid, i+1, j)
    dfs(grid, i, j-1)
    dfs(grid, i, j+1)

input = open('14.txt').read().strip()

# Partie 1 et 2
print(solve(input))