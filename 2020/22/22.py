'''
Un essai pour résoudre le jour 22 du calendrier de l'avent 2020
'''
from collections import deque

def parse_input(input):
    p1, p2 = input.strip().split('\n\n')
    p1 = deque(map(int, p1.split('\n')[1:]))
    p2 = deque(map(int, p2.split('\n')[1:]))
    return p1, p2

def combat(p1, p2):
    while p1 and p2:
        c1, c2 = p1.popleft(), p2.popleft()
        if c1 > c2:
            p1.extend([c1, c2])
        else:
            p2.extend([c2, c1])
    return p1 if p1 else p2

def recursive_combat(p1, p2, game=1):
    seen = set()
    while p1 and p2:
        config = (tuple(p1), tuple(p2))
        if config in seen:
            return p1, 'p1'
        seen.add(config)
        c1, c2 = p1.popleft(), p2.popleft()
        if len(p1) >= c1 and len(p2) >= c2:
            _, winner = recursive_combat(deque(list(p1)[:c1]), deque(list(p2)[:c2]), game + 1)
        else:
            winner = 'p1' if c1 > c2 else 'p2'
        if winner == 'p1':
            p1.extend([c1, c2])
        else:
            p2.extend([c2, c1])
    return (p1, 'p1') if p1 else (p2, 'p2')

def score(deck):
    return sum(i * card for i, card in enumerate(reversed(deck), 1))

def solve(input):
    p1, p2 = parse_input(input)
    winner = combat(p1.copy(), p2.copy())
    part1 = score(winner)
    winner, _ = recursive_combat(p1, p2)
    part2 = score(winner)
    return part1, part2

input = open('22.txt').read()

print(solve(input))