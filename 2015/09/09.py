'''
Un essai pour résoudre le jour 9 de l'année 2015
'''
from itertools import permutations

def read_distances(file_path):
    distances = {}
    cities = set()
    with open(file_path, 'r') as file:
        for line in file:
            city1, _, city2, _, distance = line.strip().split()
            distances[frozenset({city1, city2})] = int(distance)
            cities.add(city1)
            cities.add(city2)
    return distances, list(cities)

def calculate_distance(route, distances):
    return sum(distances[frozenset({route[i], route[i+1]})] for i in range(len(route) - 1))

distances, cities = read_distances('09.txt')

# Part 1
print(min(calculate_distance(route, distances) for route in permutations(cities)))

# Part 2
print(max(calculate_distance(route, distances) for route in permutations(cities)))