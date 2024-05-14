'''
Trois essais pour résoudre le jour 22 de l'Avent de Code 2017.
'''
def parse_input(input):
    grid = input.splitlines()
    height = len(grid)
    width = len(grid[0])
    return {(x-width//2, y-height//2): (1 if cell == '#' else 0) for y, row in enumerate(grid) for x, cell in enumerate(row)}

def solve(input, bursts, part2=False):
    grid = parse_input(input)
    x, y, dx, dy = 0, 0, 0, -1
    infections = 0
    for _ in range(bursts):
        cell = grid.get((x, y), 0)
        if cell == 0:  # Clean
            dx, dy = dy, -dx  # Turn left
            if part2:
                grid[x, y] = 2  # Weakened
            else:
                grid[x, y] = 1  # Infected
                infections += 1
        elif cell == 1:  # Infected
            dx, dy = -dy, dx  # Turn right
            if part2:
                grid[x, y] = 3  # Flagged
            else:
                grid[x, y] = 0  # Clean
        elif cell == 2:  # Weakened
            grid[x, y] = 1  # Infected
            infections += 1
        elif cell == 3:  # Flagged
            dx, dy = -dx, -dy  # Reverse direction
            grid[x, y] = 0  # Clean
        x, y = x + dx, y + dy
    return infections

input = open('22.txt').read()
print(solve(input, 10000))  # Part 1
print(solve(input, 10000000, part2=True))  # Part 2