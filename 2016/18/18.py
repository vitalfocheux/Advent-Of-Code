'''
Deux essais pour résoudre le jour 18 de l'Avent de Code 2016
'''
def generate_next_row(previous_row):
    next_row = ''
    for i in range(len(previous_row)):
        left = previous_row[i - 1] if i > 0 else '.'
        center = previous_row[i]
        right = previous_row[i + 1] if i < len(previous_row) - 1 else '.'
        next_row += '^' if (left == '^' and center == '^' and right == '.') or \
                            (center == '^' and right == '^' and left == '.') or \
                            (left == '^' and center == '.' and right == '.') or \
                            (right == '^' and center == '.' and left == '.') else '.'
    return next_row

def count_safe_tiles(first_row, num_rows):
    current_row = first_row
    safe_tiles = current_row.count('.')
    for _ in range(num_rows - 1):
        current_row = generate_next_row(current_row)
        safe_tiles += current_row.count('.')
    return safe_tiles

data = '...^^^^^..^...^...^^^^^^...^.^^^.^.^.^^.^^^.....^.^^^...^^^^^^.....^.^^...^^^^^...^.^^^.^^......^^^^'

# Part 1
print(count_safe_tiles(data, 40))

# Part 2
print(count_safe_tiles(data, 400000))