'''
Un essai pour résoudre le jour 1 de l'année 2017
'''
def read_input(file_path):
    with open(file_path, 'r') as file:
        return file.read().strip()

def solve_part1(input):
    total = 0
    for i in range(len(input)):
        if input[i] == input[(i+1) % len(input)]:
            total += int(input[i])
    return total

def solve_part2(input):
    total = 0
    step = len(input) // 2
    for i in range(len(input)):
        if input[i] == input[(i+step) % len(input)]:
            total += int(input[i])
    return total

input = read_input('01.txt')

# Partie 1
print(solve_part1(input))

# Partie 2
print(solve_part2(input))