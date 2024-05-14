'''
Un essai pour résoudre le jour 24
'''
def parse_input(input):
    return [tuple(map(int, line.split('/'))) for line in input.splitlines()]

def build_bridges(components, bridge=(), port=0):
    bridges = [bridge]
    for c in components:
        if port in c:
            remaining = components[:]
            remaining.remove(c)
            bridges.extend(build_bridges(remaining, bridge + (c,), c[0] if c[1] == port else c[1]))
    return bridges

def strength(bridge):
    return sum(map(sum, bridge))

def solve(input):
    components = parse_input(input)
    bridges = build_bridges(components)
    strongest = max(bridges, key=strength)
    longest = max(bridges, key=lambda b: (len(b), strength(b)))
    return strength(strongest), strength(longest)

input = open('24.txt').read()
print(solve(input))  # Part 1 and 2