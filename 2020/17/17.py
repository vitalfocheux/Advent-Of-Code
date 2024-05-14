'''
Deux essais pour résoudre le jour 17 de l'Avent de Code 2020
'''
from itertools import product

def get_neighbors_3d(x, y, z):
    for dx, dy, dz in product([-1, 0, 1], repeat=3):
        if dx != 0 or dy != 0 or dz != 0:
            yield (x + dx, y + dy, z + dz)

def get_neighbors_4d(x, y, z, w):
    for dx, dy, dz, dw in product([-1, 0, 1], repeat=4):
        if dx != 0 or dy != 0 or dz != 0 or dw != 0:
            yield (x + dx, y + dy, z + dz, w + dw)

def simulate_cubes(active_cubes, get_neighbors, cycles):
    for _ in range(cycles):
        active_neighbors = {}
        for cube in active_cubes:
            for neighbor in get_neighbors(*cube):
                active_neighbors[neighbor] = active_neighbors.get(neighbor, 0) + 1
        new_active_cubes = set()
        for cube, neighbors in active_neighbors.items():
            if cube in active_cubes and neighbors in [2, 3]:
                new_active_cubes.add(cube)
            elif cube not in active_cubes and neighbors == 3:
                new_active_cubes.add(cube)
        active_cubes = new_active_cubes
    return len(active_cubes)

def main():
    with open('17.txt', 'r') as file:
        active_cubes_3d = {(x, y, 0) for y, line in enumerate(file) for x, cell in enumerate(line.strip()) if cell == '#'}
        active_cubes_4d = {(x, y, 0, 0) for (x, y, _) in active_cubes_3d}

    print(simulate_cubes(active_cubes_3d, get_neighbors_3d, cycles=6))
    print(simulate_cubes(active_cubes_4d, get_neighbors_4d, cycles=6))

if __name__ == "__main__":
    main()