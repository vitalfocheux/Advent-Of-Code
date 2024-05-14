'''
Un essai pour la partie 1
'''
def read_coordinates(filename):
    with open(filename, 'r') as file:
        return [tuple(map(int, line.strip().split(','))) for line in file]

def calculate_surface_area(coordinates):
    cubes = set(coordinates)
    total_surface_area = 0
    for x, y, z in cubes:
        for dx, dy, dz in [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]:
            if (x + dx, y + dy, z + dz) not in cubes:
                total_surface_area += 1
    return total_surface_area

coordinates = read_coordinates('18.txt')
print(calculate_surface_area(coordinates))