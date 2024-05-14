'''
Un essai pour la partie 1
Pour la partie 2 Copilot n'est pas en mesure de trouver une solution
'''
import re

def read_input(file_name):
    with open(file_name) as f:
        lines = f.read().splitlines()
    return [list(map(int, re.findall(r'\d+', line))) for line in lines[2:]]

def part1(nodes):
    count = 0
    for a in nodes:
        for b in nodes:
            if a != b and a[3] != 0 and a[3] <= b[4]:
                count += 1
    return count

from heapq import heappop, heappush

def dijkstra(nodes, start, target):
    start = tuple(start)
    target = tuple(target)
    queue = [(0, start)]
    distances = {start: 0}
    while queue:
        (distance, current) = heappop(queue)
        if current == target:
            return distance
        for neighbor in get_neighbors(nodes, current):
            new_distance = distance + 1
            neighbor = tuple(neighbor)
            if neighbor not in distances or new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                heappush(queue, (new_distance, neighbor))

def get_neighbors(nodes, node):
    x, y = node[:2]
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nx, ny = x + dx, y + dy
        for n in nodes:
            if n[0] == nx and n[1] == ny and n[2] >= node[3]:
                yield (nx, ny, n[2], n[3], n[4])

def part2(nodes):
    target = max(nodes, key=lambda x: x[0])
    empty = next(node for node in nodes if node[3] == 0)
    distance = dijkstra(nodes, empty, target)
    if distance is None:
        return "No path found"
    return distance + (target[0] - 1) * 5 + 1

nodes = read_input('22.txt')
print("Part 1:", part1(nodes))
# print("Part 2:", part2(nodes))