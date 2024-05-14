'''
Un essai pour résoudre le jour 10 de l'année 2019 du site Advent of Code
'''
from math import atan2, pi
from collections import defaultdict

def get_asteroids(map):
    return [(x, y) for y, row in enumerate(map) for x, val in enumerate(row) if val == '#']

def get_angle_and_distance(p1, p2):
    dx, dy = p2[0] - p1[0], p1[1] - p2[1]
    return atan2(dx, dy) % (2 * pi), dx*dx + dy*dy

def get_visible_asteroids(asteroids, station):
    angles = defaultdict(list)
    for asteroid in asteroids:
        if asteroid != station:
            angle, distance = get_angle_and_distance(station, asteroid)
            angles[angle].append((distance, asteroid))
    for angle in angles:
        angles[angle].sort()
    return angles

def part1(asteroids):
    return max((len(get_visible_asteroids(asteroids, station)), station) for station in asteroids)

def part2(asteroids, station):
    visible_asteroids = get_visible_asteroids(asteroids, station)
    destroyed = 0
    while visible_asteroids:
        for angle in sorted(visible_asteroids):
            destroyed += 1
            if destroyed == 200:
                return visible_asteroids[angle][0][1]
            visible_asteroids[angle].pop(0)
            if not visible_asteroids[angle]:
                del visible_asteroids[angle]

map = [list(line.strip()) for line in open('10.txt')]
asteroids = get_asteroids(map)

# Part 1
visible, station = part1(asteroids)
print(visible)

# Part 2
x, y = part2(asteroids, station)
print(x * 100 + y)