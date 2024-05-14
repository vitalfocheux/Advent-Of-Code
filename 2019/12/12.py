'''
Deux essais pour résoudre le jour 12 de l'année 2019 du site Advent of Code
'''
from math import gcd
import re
from itertools import combinations

def lcm(a, b):
    return a * b // gcd(a, b)

def simulate(positions, velocities):
    for _ in range(1000):
        for moon1, moon2 in combinations(range(4), 2):
            for axis in range(3):
                if positions[moon1][axis] < positions[moon2][axis]:
                    velocities[moon1][axis] += 1
                    velocities[moon2][axis] -= 1
                elif positions[moon1][axis] > positions[moon2][axis]:
                    velocities[moon1][axis] -= 1
                    velocities[moon2][axis] += 1
        for moon in range(4):
            for axis in range(3):
                positions[moon][axis] += velocities[moon][axis]
    return sum(sum(abs(p) for p in positions[moon]) * sum(abs(v) for v in velocities[moon]) for moon in range(4))

def find_period(positions, velocities):
    initial_positions = [list(p) for p in positions]
    initial_velocities = [list(v) for v in velocities]
    periods = [0, 0, 0]
    steps = 0
    while not all(periods):
        for moon1, moon2 in combinations(range(4), 2):
            for axis in range(3):
                if positions[moon1][axis] < positions[moon2][axis]:
                    velocities[moon1][axis] += 1
                    velocities[moon2][axis] -= 1
                elif positions[moon1][axis] > positions[moon2][axis]:
                    velocities[moon1][axis] -= 1
                    velocities[moon2][axis] += 1
        for moon in range(4):
            for axis in range(3):
                positions[moon][axis] += velocities[moon][axis]
        steps += 1
        for axis in range(3):
            if periods[axis] == 0 and all(positions[moon][axis] == initial_positions[moon][axis] and velocities[moon][axis] == initial_velocities[moon][axis] for moon in range(4)):
                periods[axis] = steps
    return lcm(lcm(periods[0], periods[1]), periods[2])

positions = [list(map(int, re.findall(r'-?\d+', line))) for line in open('12.txt')]
velocities = [[0, 0, 0] for _ in range(4)]

# Part 1
print(simulate([list(p) for p in positions], [list(v) for v in velocities]))

# Part 2
print(find_period(positions, velocities))