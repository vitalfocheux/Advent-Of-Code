'''
Un essai pour résoudre le jour 18 de 2015
'''
def read_grid(file_path):
    with open(file_path, 'r') as file:
        return [list(line.strip()) for line in file]

def count_neighbors(grid, row, col):
    count = 0
    for i in range(max(0, row - 1), min(len(grid), row + 2)):
        for j in range(max(0, col - 1), min(len(grid[0]), col + 2)):
            if (i, j) != (row, col) and grid[i][j] == '#':
                count += 1
    return count

def next_state(grid, part2=False):
    new_grid = [row.copy() for row in grid]
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            neighbors = count_neighbors(grid, i, j)
            if grid[i][j] == '#':
                if neighbors not in [2, 3]:
                    new_grid[i][j] = '.'
            else:
                if neighbors == 3:
                    new_grid[i][j] = '#'
    if part2:
        for i, j in [(0, 0), (0, len(grid[0]) - 1), (len(grid) - 1, 0), (len(grid) - 1, len(grid[0]) - 1)]:
            new_grid[i][j] = '#'
    return new_grid

def solve_part1(grid):
    for _ in range(100):
        grid = next_state(grid)
    return sum(row.count('#') for row in grid)

def solve_part2(grid):
    for i, j in [(0, 0), (0, len(grid[0]) - 1), (len(grid) - 1, 0), (len(grid) - 1, len(grid[0]) - 1)]:
        grid[i][j] = '#'
    for _ in range(100):
        grid = next_state(grid, True)
    return sum(row.count('#') for row in grid)

grid = read_grid('18.txt')

# Part 1
print(solve_part1(grid))

# Part 2
print(solve_part2(grid))