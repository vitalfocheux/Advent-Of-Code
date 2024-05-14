'''
Un essai pour résoudre le jour 3 de l'année 2019
'''
def parse_input(input_lines):
    return [line.split(',') for line in input_lines]

def trace_wire(path):
    DIRECTIONS = {'U': (0, 1), 'D': (0, -1), 'L': (-1, 0), 'R': (1, 0)}
    x, y, length = 0, 0, 0
    wire = {}
    for segment in path:
        dx, dy = DIRECTIONS[segment[0]]
        for _ in range(int(segment[1:])):
            x += dx
            y += dy
            length += 1
            if (x, y) not in wire:
                wire[(x, y)] = length
    return wire

def part1(input_lines):
    paths = parse_input(input_lines)
    wires = list(map(trace_wire, paths))
    intersections = set(wires[0].keys()) & set(wires[1].keys())
    return min(abs(x) + abs(y) for (x, y) in intersections)

def part2(input_lines):
    paths = parse_input(input_lines)
    wires = list(map(trace_wire, paths))
    intersections = set(wires[0].keys()) & set(wires[1].keys())
    return min(wires[0][point] + wires[1][point] for point in intersections)

# Test the program with your input
with open('03.txt') as f:
    input_lines = f.readlines()
print(part1(input_lines))  # Part 1
print(part2(input_lines))  # Part 2