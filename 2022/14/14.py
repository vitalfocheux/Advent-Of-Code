'''
Un essai avec Llama3-70b-8192 pour résoudre le jour 14 de 2022
'''
def parse_cave_scan(file_name):
    cave = {}
    with open(file_name, 'r') as f:
        for line in f:
            points = [tuple(map(int, point.split(','))) for point in line.strip().split(' -> ')]
            for i in range(len(points) - 1):
                x1, y1 = points[i]
                x2, y2 = points[i + 1]
                if x1 == x2:
                    for y in range(min(y1, y2), max(y1, y2) + 1):
                        cave[(x1, y)] = '#'
                elif y1 == y2:
                    for x in range(min(x1, x2), max(x1, x2) + 1):
                        cave[(x, y1)] = '#'
    return cave

def simulate_sand(cave):
    sand_count = 0
    while True:
        sand_x, sand_y = 500, 0
        while True:
            if (sand_x, sand_y + 1) not in cave:
                sand_y += 1
            elif (sand_x - 1, sand_y + 1) not in cave:
                sand_x -= 1
                sand_y += 1
            elif (sand_x + 1, sand_y + 1) not in cave:
                sand_x += 1
                sand_y += 1
            else:
                cave[(sand_x, sand_y)] = 'o'
                sand_count += 1
                break
            if sand_y > max(y for x, y in cave):
                return sand_count

cave = parse_cave_scan('14.txt')
print(simulate_sand(cave))

def parse_cave_scan(file_name):
    cave = {}
    max_y = 0
    with open(file_name, 'r') as f:
        for line in f:
            points = [tuple(map(int, point.split(','))) for point in line.strip().split(' -> ')]
            for i in range(len(points) - 1):
                x1, y1 = points[i]
                x2, y2 = points[i + 1]
                if x1 == x2:
                    for y in range(min(y1, y2), max(y1, y2) + 1):
                        cave[(x1, y)] = '#'
                        max_y = max(max_y, y)
                elif y1 == y2:
                    for x in range(min(x1, x2), max(x1, x2) + 1):
                        cave[(x, y1)] = '#'
                        max_y = max(max_y, y1)
    floor_y = max_y + 2
    for x in range(-1000, 1000):
        cave[(x, floor_y)] = '#'
    return cave

def simulate_sand(cave):
    sand_count = 0
    while True:
        sand_x, sand_y = 500, 0
        while True:
            if (sand_x, sand_y + 1) not in cave:
                sand_y += 1
            elif (sand_x - 1, sand_y + 1) not in cave:
                sand_x -= 1
                sand_y += 1
            elif (sand_x + 1, sand_y + 1) not in cave:
                sand_x += 1
                sand_y += 1
            else:
                cave[(sand_x, sand_y)] = 'o'
                sand_count += 1
                if (sand_x, sand_y) == (500, 0):
                    return sand_count
                break

cave = parse_cave_scan('14.txt')
print(simulate_sand(cave))