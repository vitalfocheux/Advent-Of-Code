'''
Copilot essayait de faire les deux parties avec une fonction -> ne fonctionnait toujours pas au bout de cinq essais
En lui demandant de faire une fonction pour chaque partie si nécéssaire, il a réussi à résoudre le problème en un essai
'''
import re

def read_sues(file_path):
    sues = {}
    with open(file_path, 'r') as file:
        for line in file:
            sue, *items = re.findall(r'Sue (\d+): (\w+): (\d+), (\w+): (\d+), (\w+): (\d+)', line)[0]
            sues[int(sue)] = {items[i]: int(items[i+1]) for i in range(0, len(items), 2)}
    return sues

def find_sue_part1(sues, description):
    for sue, items in sues.items():
        if all(description[item] == value for item, value in items.items() if item in description):
            return sue

def find_sue_part2(sues, description):
    for sue, items in sues.items():
        if all((description[item] == value if item not in ['cats', 'trees', 'pomeranians', 'goldfish'] else
                (description[item] < value if item in ['cats', 'trees'] else description[item] > value))
               for item, value in items.items() if item in description):
            return sue

description = {'children': 3, 'cats': 7, 'samoyeds': 2, 'pomeranians': 3, 'akitas': 0, 'vizslas': 0, 'goldfish': 5, 'trees': 3, 'cars': 2, 'perfumes': 1}

sues = read_sues('16.txt')

# Part 1
print(find_sue_part1(sues, description))

# Part 2
print(find_sue_part2(sues, description))