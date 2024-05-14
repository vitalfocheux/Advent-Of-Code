'''
Un essai pour la partie 1
La partie 2 ne fonctionne pas
'''
from heapq import heappop, heappush

def calculate_erosion_levels(depth, target, padding=50):
    erosion_levels = {}
    for y in range(target[1] + padding + 1):
        for x in range(target[0] + padding + 1):
            if (x, y) in [(0, 0), target]:
                geo_index = 0
            elif y == 0:
                geo_index = x * 16807
            elif x == 0:
                geo_index = y * 48271
            else:
                geo_index = erosion_levels[(x-1, y)] * erosion_levels[(x, y-1)]
            erosion_level = (geo_index + depth) % 20183
            erosion_levels[(x, y)] = erosion_level
    return erosion_levels

def shortest_path(erosion_levels, target):
    queue = [(0, 0, 0, 1)]  # time, x, y, equipment
    visited = set([(0, 0, 1)])
    while queue:
        time, x, y, equipment = heappop(queue)
        if (x, y, equipment) == (target[0], target[1], 1):
            return time
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            new_x, new_y = x + dx, y + dy
            if new_x < 0 or new_y < 0 or (new_x, new_y) not in erosion_levels:
                continue
            if erosion_levels[(new_x, new_y)] % 3 != equipment:
                if (new_x, new_y, equipment) not in visited:
                    visited.add((new_x, new_y, equipment))
                    heappush(queue, (time + 1, new_x, new_y, equipment))
        for new_equipment in [0, 1, 2]:
            if new_equipment != equipment and new_equipment != erosion_levels[(x, y)] % 3:
                if (x, y, new_equipment) not in visited:
                    visited.add((x, y, new_equipment))
                    heappush(queue, (time + 7, x, y, new_equipment))
    return None

depth = 11109  # replace with your input
target = (9, 731)  # replace with your input
erosion_levels = calculate_erosion_levels(depth, target)
print(sum(erosion_levels[(x, y)] % 3 for x in range(target[0] + 1) for y in range(target[1] + 1)))  # Part 1
print(shortest_path(erosion_levels, target))  # Part 2