'''
Un essai pour la partie 1
La partie 2 au bout de plus 10 essais ne fonctionne pas
'''
import re
from collections import defaultdict

def parse_input(input):
    particles = []
    for line in input.splitlines():
        p, v, a = map(eval, re.findall('<(.*?)>', line))
        particles.append([list(p), list(v), list(a)])
    return particles

def solve_part1(particles):
    for _ in range(1000):  # Assume particles have stabilized after 1000 updates
        for i, (p, v, a) in enumerate(particles):
            v = [v[j] + a[j] for j in range(3)]
            p = [p[j] + v[j] for j in range(3)]
            particles[i] = [p, v, a]
    return min(range(len(particles)), key=lambda i: sum(map(abs, particles[i][0])))

def solve_part2(particles):
    for _ in range(1000):  # Assume particles have stabilized after 1000 updates
        positions = defaultdict(list)
        # Update all particles first
        for i, (p, v, a) in enumerate(particles):
            v = tuple(v[j] + a[j] for j in range(3))
            p = tuple(p[j] + v[j] for j in range(3))
            particles[i] = (p, v, a)
        # Then detect collisions
        for i, (p, v, a) in enumerate(particles):
            positions[p].append(i)
        collided = {i for indices in positions.values() if len(indices) > 1 for i in indices}
        particles = [particle for i, particle in enumerate(particles) if i not in collided]
    return len(particles)

input = open('20.txt').read()
particles = parse_input(input)
print(solve_part1(particles))  # Part 1
print(solve_part2(particles))  # Part 2