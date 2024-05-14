'''
Un essai pour résoudre le jour 9 de 2017
'''
def solve(input):
    score = 0
    garbage_count = 0
    depth = 0
    garbage = False
    skip = False
    for char in input:
        if skip:
            skip = False
            continue
        if char == '!':
            skip = True
        elif garbage:
            if char == '>':
                garbage = False
            else:
                garbage_count += 1
        elif char == '<':
            garbage = True
        elif char == '{':
            depth += 1
            score += depth
        elif char == '}':
            depth -= 1
    return score, garbage_count

input = open('09.txt').read()

# Partie 1 et 2
print(solve(input.strip()))