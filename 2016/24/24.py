'''
Cinq essais pour résoudre le problème du jour 24.
'''
import itertools
from collections import deque

def read_input(file_path):
    with open(file_path) as f:
        return [list(line.strip()) for line in f]

def bfs(grid, start, end):
    queue = deque([(start, 0)])
    visited = {start}
    while queue:
        pos, steps = queue.popleft()
        x, y = pos
        if (x, y) == end:
            return steps
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if grid[nx][ny] != '#' and (nx, ny) not in visited:
                queue.append(((nx, ny), steps + 1))
                visited.add((nx, ny))

def solve(grid, return_to_start):
    points = {(x, y): int(grid[x][y])
              for x in range(len(grid))
              for y in range(len(grid[0]))
              if grid[x][y].isdigit()}
    start_point = [point for point, value in points.items() if value == 0][0]
    distances = {(a, b): bfs(grid, a, b)
                 for a in points for b in points if a != b}
    paths = itertools.permutations([point for point in points.keys() if point != start_point])
    return min(sum(distances[a, b] for a, b in zip((start_point,) + path, path + ((start_point,) if return_to_start else ())))
               for path in paths)

grid = read_input('24.txt')

# Part 1
print(solve(grid, False))

# Part 2
print(solve(grid, True))