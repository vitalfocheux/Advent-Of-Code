'''
Un essai pour résoudre le jour 10 de l'année 2015
'''
import re

def look_and_say(sequence):
    return ''.join(f'{len(match.group())}{match.group()[0]}' for match in re.finditer(r'(\d)\1*', sequence))

def iterate_look_and_say(sequence, iterations):
    for _ in range(iterations):
        sequence = look_and_say(sequence)
    return sequence

with open('10.txt', 'r') as file:
    sequence = file.read().strip()

# Part 1
print(len(iterate_look_and_say(sequence, 40)))

# Part 2
print(len(iterate_look_and_say(sequence, 50)))