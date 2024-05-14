'''
Un essai pour résoudre le problème 25 de 2018
'''
def parse_input(input_lines):
    return [list(map(int, line.split(','))) for line in input_lines]

def manhattan_distance(p1, p2):
    return sum(abs(a - b) for a, b in zip(p1, p2))

def are_connected(p1, p2):
    return manhattan_distance(p1, p2) <= 3

def find_constellations(points):
    constellations = []
    for point in points:
        connected = []
        for constellation in constellations:
            if any(are_connected(point, p) for p in constellation):
                connected.append(constellation)
        for constellation in connected:
            constellations.remove(constellation)
        constellations.append(sum(connected, [point]))
    return constellations

def part1(input_lines):
    points = parse_input(input_lines)
    constellations = find_constellations(points)
    return len(constellations)

# Test the program with your input
with open('25.txt') as f:
    input_lines = f.readlines()
print(part1(input_lines))  # Part 1 and 2