'''
Deux essais pour résoudre le jour 25
'''
import re

def parse_input(input):
    lines = input.splitlines()
    state = re.findall(r'Begin in state (\w).', lines[0])[0]
    steps = int(re.findall(r'Perform a diagnostic checksum after (\d+) steps.', lines[1])[0])
    states = {}
    for i in range(3, len(lines), 10):
        name = re.findall(r'In state (\w):', lines[i])[0]
        values = list(map(int, re.findall(r'- Write the value (\d).', '\n'.join(lines[i:i+10]))))
        directions = ['right' if d == 'right' else 'left' for d in re.findall(r'- Move one slot to the (\w+).', '\n'.join(lines[i:i+10]))]
        next_states = re.findall(r'- Continue with state (\w).', '\n'.join(lines[i:i+10]))
        states[name] = list(zip(values, directions, next_states))
    return state, steps, states

def run(state, steps, states):
    tape = {}
    cursor = 0
    for _ in range(steps):
        if cursor not in tape:
            tape[cursor] = 0
        value, direction, next_state = states[state][tape[cursor]]
        tape[cursor] = value
        cursor += 1 if direction == 'right' else -1
        state = next_state
    return list(tape.values()).count(1)

input = open('25.txt').read()
state, steps, states = parse_input(input)
print(run(state, steps, states))  # Part 1