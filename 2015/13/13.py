'''
Un essai pour résoudre le jour 13 de l'année 2015
'''
from itertools import permutations

def read_preferences(file_path):
    preferences = {}
    guests = set()
    with open(file_path, 'r') as file:
        for line in file:
            parts = line.strip()[:-1].split()
            guest1, _, sign, value, _, _, _, _, _, _, guest2 = parts
            if sign == 'lose':
                value = -int(value)
            else:
                value = int(value)
            preferences[(guest1, guest2)] = value
            guests.add(guest1)
    return preferences, list(guests)

def calculate_happiness(arrangement, preferences):
    happiness = 0
    for i in range(len(arrangement)):
        guest1 = arrangement[i]
        guest2 = arrangement[(i+1) % len(arrangement)]
        happiness += preferences.get((guest1, guest2), 0)
        happiness += preferences.get((guest2, guest1), 0)
    return happiness

preferences, guests = read_preferences('13.txt')

# Part 1
print(max(calculate_happiness(arrangement, preferences) for arrangement in permutations(guests)))

# Part 2
guests.append('me')
print(max(calculate_happiness(arrangement, preferences) for arrangement in permutations(guests)))