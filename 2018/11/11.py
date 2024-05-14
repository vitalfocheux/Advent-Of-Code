'''
Un essai pour la partie 1
Trois essais pour la partie 2
'''
def calculate_power(x, y, serial):
    rack_id = x + 10
    power_level = rack_id * y
    power_level += serial
    power_level *= rack_id
    power_level = (power_level // 100) % 10
    power_level -= 5
    return power_level

def calculate_grid(serial):
    return [[calculate_power(x+1, y+1, serial) for x in range(300)] for y in range(300)]

def calculate_square_power(x, y, size, grid):
    return sum(grid[y+i][x+j] for i in range(size) for j in range(size))

def part1(grid):
    max_power = float('-inf')
    max_coords = None
    for y in range(300-3):
        for x in range(300-3):
            power = calculate_square_power(x, y, 3, grid)
            if power > max_power:
                max_power = power
                max_coords = (x+1, y+1)
    return max_coords

def calculate_integral_image(grid):
    integral_image = [[0]*301 for _ in range(301)]
    for y in range(300):
        for x in range(300):
            integral_image[y+1][x+1] = grid[y][x] + integral_image[y][x+1] + integral_image[y+1][x] - integral_image[y][x]
    return integral_image

def calculate_square_power2(x, y, size, integral_image):
    return integral_image[y+size][x+size] - integral_image[y+size][x] - integral_image[y][x+size] + integral_image[y][x]

def part2(grid):
    integral_image = calculate_integral_image(grid)
    max_power = float('-inf')
    max_coords = None
    for size in range(1, 301):
        for y in range(300-size+1):
            for x in range(300-size+1):
                power = calculate_square_power2(x, y, size, integral_image)
                if power > max_power:
                    max_power = power
                    max_coords = (x+1, y+1, size)
    return max_coords

serial = 3214  # replace with your puzzle input
grid = calculate_grid(serial)
print(part1(grid))  # solution for part 1
print(part2(grid))  # solution for part 2