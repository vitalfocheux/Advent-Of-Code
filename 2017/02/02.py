'''
Un essai pour résoudre le jour 2 de l'Avent of Code 2017
'''
def read_input(file_path):
    with open(file_path, 'r') as file:
        return [[int(num) for num in line.split()] for line in file]

def solve_part1(input):
    return sum(max(row) - min(row) for row in input)

def solve_part2(input):
    total = 0
    for row in input:
        for i in range(len(row)):
            for j in range(i+1, len(row)):
                if row[i] % row[j] == 0:
                    total += row[i] // row[j]
                elif row[j] % row[i] == 0:
                    total += row[j] // row[i]
    return total

input = read_input('02.txt')

# Partie 1
print(solve_part1(input))

# Partie 2
print(solve_part2(input))