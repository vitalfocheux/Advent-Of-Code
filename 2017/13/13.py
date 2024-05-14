'''
Un essai pour résoudre le jour 13 de 2017
'''
def parse_input(input):
    firewall = {}
    for line in input.split('\n'):
        depth, range = map(int, line.split(': '))
        firewall[depth] = range
    return firewall

def solve_part1(firewall):
    severity = 0
    for depth, range in firewall.items():
        if depth % ((range - 1) * 2) == 0:
            severity += depth * range
    return severity

def solve_part2(firewall):
    delay = 0
    while any((depth + delay) % ((range - 1) * 2) == 0 for depth, range in firewall.items()):
        delay += 1
    return delay

input = open('13.txt').read()

firewall = parse_input(input.strip())

# Partie 1
print(solve_part1(firewall))

# Partie 2
print(solve_part2(firewall))