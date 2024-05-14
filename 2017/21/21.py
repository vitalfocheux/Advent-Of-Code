'''
Cinq essais pour résoudre le jour 21
'''
def rotate(grid):
    return [''.join(x[::-1]) for x in zip(*grid)]

def flip(grid):
    return [x[::-1] for x in grid]

def get_variations(pattern):
    pattern = pattern.split('/')
    variations = [pattern]
    for _ in range(3):
        pattern = rotate(pattern)
        variations.append(pattern)
        variations.append(flip(pattern))
    return ['/'.join(v) for v in variations]

def parse_input(input):
    rules = {}
    for line in input.splitlines():
        src, dst = line.split(" => ")
        for var in get_variations(src):
            rules[var] = dst
    return rules

def split_grid(grid):
    size = len(grid)
    new_size = 2 if size % 2 == 0 else 3
    squares = []
    for i in range(0, size, new_size):
        for j in range(0, size, new_size):
            square = [''.join(grid[i+k][j:j+new_size]) for k in range(new_size)]
            squares.append('/'.join(square))
    return squares

def join_grid(squares):
    size = int(len(squares)**0.5)
    new_size = len(squares[0].split('/'))
    grid = [['' for _ in range(size*new_size)] for _ in range(size*new_size)]
    for i in range(size):
        for j in range(size):
            square = squares[i*size+j].split('/')
            for k in range(new_size):
                grid[i*new_size+k][j*new_size:(j+1)*new_size] = square[k]
    return [''.join(row) for row in grid]

def transform(grid, rules):
    squares = split_grid(grid)
    squares = [rules[square] for square in squares]
    return join_grid(squares)

def solve(input, iterations):
    rules = parse_input(input)
    grid = [list(".#."), list("..#"), list("###")]
    for _ in range(iterations):
        grid = transform(grid, rules)
    return sum(row.count('#') for row in grid)

input = open('21.txt').read()
print(solve(input, 5))  # Part 1
print(solve(input, 18))  # Part 2