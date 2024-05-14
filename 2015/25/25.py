def read(filename):
    with open(filename, 'r') as file:
        line = file.readline().strip()
        row = int(line.split()[-3][:-1])
        col = int(line.split()[-1][:-1])
    return row, col

def calculate_code(row, col):
    code = 20151125
    n = sum(range(row + col - 1)) + col
    for _ in range(n - 1):
        code = (code * 252533) % 33554393
    return code

def solve_part1(filename):
    row, col = read(filename)
    return calculate_code(row, col)

# Read from file and solve part 1
print(solve_part1('25.txt'))