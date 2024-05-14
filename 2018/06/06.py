from collections import defaultdict

def manhattan_distance(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

def solve_part1(coordinates):
    min_x = min(x for x, _ in coordinates)
    max_x = max(x for x, _ in coordinates)
    min_y = min(y for _, y in coordinates)
    max_y = max(y for _, y in coordinates)

    closest = defaultdict(int)
    infinite = set()

    for x in range(min_x, max_x + 1):
        for y in range(min_y, max_y + 1):
            distances = sorted((manhattan_distance((x, y), coord), i) for i, coord in enumerate(coordinates))
            if distances[0][0] != distances[1][0]:
                closest[distances[0][1]] += 1
                if x == min_x or x == max_x or y == min_y or y == max_y:
                    infinite.add(distances[0][1])

    return max(area for i, area in closest.items() if i not in infinite)

def solve_part2(coordinates, limit=10000):
    min_x = min(x for x, _ in coordinates)
    max_x = max(x for x, _ in coordinates)
    min_y = min(y for _, y in coordinates)
    max_y = max(y for _, y in coordinates)

    size = 0
    for x in range(min_x, max_x + 1):
        for y in range(min_y, max_y + 1):
            if sum(manhattan_distance((x, y), coord) for coord in coordinates) < limit:
                size += 1

    return size

# Assuming coordinates is a list of tuples read from the input file
with open('06.txt', 'r') as file:
    coordinates = [tuple(map(int, line.split(', '))) for line in file]

print(solve_part1(coordinates))  # Part 1
print(solve_part2(coordinates))  # Part 2