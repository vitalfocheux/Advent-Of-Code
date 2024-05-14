'''
Trois essais pour résoudre le jour 12 de l'année 2018
'''
def parse_input(input):
    lines = input.splitlines()
    initial_state = {i: c for i, c in enumerate(lines[0][15:])}
    rules = {line[:5]: line[9] for line in lines[2:]}
    return initial_state, rules

def next_generation(state, rules):
    min_pot = min(state.keys())
    max_pot = max(state.keys())
    new_state = {}
    for i in range(min_pot - 2, max_pot + 3):
        pattern = ''.join(state.get(j, '.') for j in range(i - 2, i + 3))
        new_state[i] = rules.get(pattern, '.')
    return new_state

def sum_plants(state):
    return sum(i for i, c in state.items() if c == '#')

def solve(input, generations):
    state, rules = parse_input(input)
    for _ in range(generations):
        state = next_generation(state, rules)
    return sum_plants(state)

def solve_part2(input):
    state, rules = parse_input(input)
    prev_diff, prev_total = 0, 0
    for generation in range(1, 50000000000 + 1):
        state = next_generation(state, rules)
        total = sum_plants(state)
        diff = total - prev_total
        if diff == prev_diff:
            return total + diff * (50000000000 - generation)
        prev_diff, prev_total = diff, total

input = open('12.txt').read().strip()
print(solve(input, 20))  # solution for part 1
print(solve_part2(input))  # solution for part 2