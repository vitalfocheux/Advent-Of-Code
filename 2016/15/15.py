'''
Un essai pour résoudre le jour 15 de l'Avent de Code 2016
'''
def read_input(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    discs = []
    for line in lines:
        parts = line.split()
        positions = int(parts[3])
        start = int(parts[-1][:-1])
        discs.append((positions, start))
    return discs

def find_start_time(discs):
    time = 0
    while True:
        if all((start + time + i + 1) % positions == 0 for i, (positions, start) in enumerate(discs)):
            return time
        time += 1

discs = read_input('15.txt')

# Part 1
print(find_start_time(discs))

# Part 2
discs.append((11, 0))
print(find_start_time(discs))