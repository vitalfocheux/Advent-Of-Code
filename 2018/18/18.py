'''
Un essai pour la partie 1
Deux essais pour la partie 2 car le première n'était pas optimisé
'''
def parse_input(input):
    return [list(line) for line in input]

def count_neighbors(grid, x, y, target):
    count = 0
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            if dx == dy == 0:
                continue
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny] == target:
                count += 1
    return count

def evolve(grid):
    new_grid = [row[:] for row in grid]
    for x, row in enumerate(grid):
        for y, acre in enumerate(row):
            if acre == '.' and count_neighbors(grid, x, y, '|') >= 3:
                new_grid[x][y] = '|'
            elif acre == '|' and count_neighbors(grid, x, y, '#') >= 3:
                new_grid[x][y] = '#'
            elif acre == '#' and (count_neighbors(grid, x, y, '#') == 0 or count_neighbors(grid, x, y, '|') == 0):
                new_grid[x][y] = '.'
    return new_grid

def solve(input, minutes):
    grid = parse_input(input)
    seen = {}
    for minute in range(1, minutes + 1):
        grid = evolve(grid)
        state = str(grid)
        if state in seen:
            cycle_length = minute - seen[state]
            remaining_minutes = (minutes - minute) % cycle_length
            for _ in range(remaining_minutes):
                grid = evolve(grid)
            break
        else:
            seen[state] = minute
    wooded = sum(acre == '|' for row in grid for acre in row)
    lumberyards = sum(acre == '#' for row in grid for acre in row)
    return wooded * lumberyards

with open('18.txt') as f:
    input = f.read().splitlines()
    print(solve(input, 10))  # Part 1
    print(solve(input, 1000000000))  # Part 2