'''
Trois essais pour résoudre le jour 15 de l'Avent de Code 2017.
'''
from itertools import islice

def generate(start, factor, multiple_of=1):
    value = start
    while True:
        value = (value * factor) % 2147483647
        if value % multiple_of == 0:
            yield value

def solve(start_a, start_b, rounds, multiple_a=1, multiple_b=1):
    gen_a = generate(start_a, 16807, multiple_a)
    gen_b = generate(start_b, 48271, multiple_b)
    return sum(a & 0xFFFF == b & 0xFFFF for a, b in zip(islice(gen_a, rounds), islice(gen_b, rounds)))

start_a, start_b = map(int, open('15.txt').read().split())

# Partie 1
print(solve(start_a, start_b, 40000000))

# Partie 2
print(solve(start_a, start_b, 5000000, 4, 8))