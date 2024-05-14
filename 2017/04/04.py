'''
Un essai pour résoudre le jour 4 de l'Avent of Code 2017
'''
def solve_part1(input):
    valid_phrases = 0
    for line in input:
        words = line.split()
        if len(words) == len(set(words)):
            valid_phrases += 1
    return valid_phrases

def solve_part2(input):
    valid_phrases = 0
    for line in input:
        words = [''.join(sorted(word)) for word in line.split()]
        if len(words) == len(set(words)):
            valid_phrases += 1
    return valid_phrases

input = open('04.txt').read().strip().split('\n')

# Partie 1
print(solve_part1(input))

# Partie 2
print(solve_part2(input))