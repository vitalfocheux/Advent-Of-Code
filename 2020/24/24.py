'''
Deux essais pour résoudre le jour 24 du calendrier de l'avent 2020
'''
from collections import defaultdict

DIRECTIONS = {'e': (1, -1, 0), 'w': (-1, 1, 0), 'ne': (1, 0, -1), 'sw': (-1, 0, 1), 'nw': (0, 1, -1), 'se': (0, -1, 1)}

def parse_input(input):
    lines = input.strip().split('\n')
    tiles = []
    for line in lines:
        tile = []
        while line:
            if line[:2] in DIRECTIONS:
                tile.append(DIRECTIONS[line[:2]])
                line = line[2:]
            else:
                tile.append(DIRECTIONS[line[:1]])
                line = line[1:]
        tiles.append(tile)
    return tiles

def flip_tiles(tiles):
    grid = defaultdict(bool)
    for tile in tiles:
        x, y, z = map(sum, zip(*tile))
        grid[(x, y, z)] = not grid[(x, y, z)]
    return grid

def count_black_tiles(grid):
    return sum(grid.values())

def get_neighbors(tile):
    return [(tile[0] + dx, tile[1] + dy, tile[2] + dz) for dx, dy, dz in DIRECTIONS.values()]

def flip_tiles_day(grid):
    new_grid = grid.copy()
    tiles_to_check = set(tile for tile in grid if grid[tile])
    tiles_to_check_copy = tiles_to_check.copy()
    for tile in tiles_to_check_copy:
        tiles_to_check.update(get_neighbors(tile))
    for tile in tiles_to_check:
        black_neighbors = sum(grid[neighbor] for neighbor in get_neighbors(tile))
        if grid[tile] and (black_neighbors == 0 or black_neighbors > 2):
            new_grid[tile] = False
        elif not grid[tile] and black_neighbors == 2:
            new_grid[tile] = True
    return new_grid

def solve(input):
    tiles = parse_input(input)
    grid = flip_tiles(tiles)
    part1 = count_black_tiles(grid)
    for _ in range(100):
        grid = flip_tiles_day(grid)
    part2 = count_black_tiles(grid)
    return part1, part2

input = open('24.txt').read()

print(solve(input))