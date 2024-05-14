'''
Un essai pour résoudre le jour 12 de 2017
'''
def parse_input(input):
    connections = {}
    for line in input.split('\n'):
        program, connected = line.split(' <-> ')
        connections[int(program)] = list(map(int, connected.split(', ')))
    return connections

def find_group(program, connections):
    group = set([program])
    stack = [program]
    while stack:
        program = stack.pop()
        for connected in connections[program]:
            if connected not in group:
                group.add(connected)
                stack.append(connected)
    return group

def solve(input):
    connections = parse_input(input)
    group0 = find_group(0, connections)
    groups = 1
    for program in set(connections.keys()) - group0:
        if program not in group0:
            group0 |= find_group(program, connections)
            groups += 1
    return len(find_group(0, connections)), groups

input = open('12.txt').read()

# Partie 1 et 2
print(solve(input.strip()))