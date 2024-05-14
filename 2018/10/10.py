'''
Cinq essais pour résoudre le jour 10 de l'année 2018
'''
import re

def parse_input(input):
    points = []
    for line in input.splitlines():
        x, y, vx, vy = map(int, re.findall(r'-?\d+', line))
        points.append([[x, y], [vx, vy]])
    return points

def simulate(points):
    for point in points:
        point[0][0] += point[1][0]
        point[0][1] += point[1][1]
    return points

def print_message(points):
    min_x = min(point[0][0] for point in points)
    max_x = max(point[0][0] for point in points)
    min_y = min(point[0][1] for point in points)
    max_y = max(point[0][1] for point in points)

    sky = [[' ' for _ in range(max_x - min_x + 1)] for _ in range(max_y - min_y + 1)]
    for point in points:
        sky[point[0][1] - min_y][point[0][0] - min_x] = '#'

    for row in sky:
        print(''.join(row))

def solve(input):
    points = parse_input(input)
    for seconds in range(100000):
        points = simulate(points)
        min_y = min(point[0][1] for point in points)
        max_y = max(point[0][1] for point in points)
        if max_y - min_y < 10:  # adjust this value based on your input
            print(f"Message appears after {(seconds+1)} seconds:")
            print_message(points)
            break


input = open('10.txt').read().strip()
solve(input)