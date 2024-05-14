'''
Un essai pour résoudre la première partie du problème du jour 3.
Deux essais pour résoudre la deuxième partie du problème du jour 3.
'''

def read_triangles(file_path):
    with open(file_path, 'r') as file:
        return [list(map(int, line.split())) for line in file.read().splitlines()]

def is_valid(triangle):
    a, b, c = sorted(triangle)
    return a + b > c

def count_valid_triangles(triangles):
    return sum(is_valid(triangle) for triangle in triangles)

def transpose_triangles(triangles):
    transposed = []
    for i in range(0, len(triangles), 3):
        for j in range(len(triangles[0])):
            transposed.append([triangles[i+k][j] for k in range(3)])
    return transposed

triangles = read_triangles('03.txt')

# Part 1
print(count_valid_triangles(triangles))

# Part 2
transposed_triangles = transpose_triangles(triangles)
print(count_valid_triangles(transposed_triangles))