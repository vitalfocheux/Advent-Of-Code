'''
Un essai pour résoudre le jour 10 de 2017
'''
from functools import reduce
from operator import xor
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

def solve_part1(input):
    numbers = list(range(256))
    lengths = list(map(int, input.split(',')))
    numbers, _, _ = knot_hash_round(numbers, lengths)
    return numbers[0] * numbers[1]

def knot_hash(input):
    numbers = list(range(256))
    lengths = [ord(c) for c in input] + [17, 31, 73, 47, 23]
    current_position = skip_size = 0
    for _ in range(64):
        numbers, current_position, skip_size = knot_hash_round(numbers, lengths, current_position, skip_size)
    dense_hash = [reduce(xor, numbers[i*16:(i+1)*16]) for i in range(16)]
    return ''.join(f'{num:02x}' for num in dense_hash)

input = open('10.txt').read().strip()

# Partie 1
print(solve_part1(input))

# Partie 2
print(knot_hash(input))