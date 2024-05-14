'''
Un essai pour résoudre le jour 9 de Advent of Code 2018
'''
from heapq import nlargest
from collections import deque

def parse_heightmap(heightmap):
    return [[int(height) for height in row] for row in heightmap.splitlines()]

def find_low_points(matrix):
    low_points = []
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            height = matrix[i][j]
            neighbors = [
                matrix[x][y]
                for x in range(max(0, i - 1), min(i + 2, len(matrix)))
                for y in range(max(0, j - 1), min(j + 2, len(matrix[i])))
                if (x, y) != (i, j)
            ]
            if all(height <= neighbor for neighbor in neighbors):
                low_points.append((i, j))
    return low_points

def calculate_risk(low_points, matrix):
    return sum(matrix[i][j] + 1 for i, j in low_points)

def find_basins(matrix, low_points):
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    visited = [[False]*len(matrix[0]) for _ in range(len(matrix))]
    basins = []
    
    for x, y in low_points:
        if visited[x][y]:
            continue
        basin_size = 0
        queue = deque([(x, y)])
        while queue:
            i, j = queue.popleft()
            if visited[i][j]:
                continue
            visited[i][j] = True
            basin_size += 1
            for dx, dy in directions:
                ni, nj = i + dx, j + dy
                if 0 <= ni < len(matrix) and 0 <= nj < len(matrix[0]) and matrix[ni][nj] < 9 and not visited[ni][nj]:
                    queue.append((ni, nj))
        basins.append(basin_size)
    return basins

def solve(heightmap):
    matrix = parse_heightmap(heightmap)
    low_points = find_low_points(matrix)
    risk = calculate_risk(low_points, matrix)
    basins = find_basins(matrix, low_points)
    largest_basins = nlargest(3, basins)
    return risk, largest_basins[0] * largest_basins[1] * largest_basins[2]

print(solve(open("09.txt").read()))