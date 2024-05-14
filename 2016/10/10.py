'''
Sept essais pour résoudre le problème 10 de Advent of Code 2016
'''
import re
from collections import defaultdict

def read_instructions(file_path):
    with open(file_path, 'r') as file:
        return file.read().splitlines()

def execute_instructions(instructions):
    bots = defaultdict(list)
    outputs = defaultdict(list)
    instructions_to_execute = instructions[:]
    part1 = None
    while instructions_to_execute:
        for instruction in instructions_to_execute[:]:
            if match := re.match(r'value (\d+) goes to bot (\d+)', instruction):
                value, bot = map(int, match.groups())
                bots[bot].append(value)
                instructions_to_execute.remove(instruction)
            elif match := re.match(r'bot (\d+) gives low to (bot|output) (\d+) and high to (bot|output) (\d+)', instruction):
                bot, low_type, low_id, high_type, high_id = match.groups()
                bot, low_id, high_id = map(int, [bot, low_id, high_id])
                if len(bots[bot]) < 2:
                    continue
                low_value, high_value = sorted(bots[bot])
                if [low_value, high_value] == [17, 61]:
                    part1 = bot
                (bots if low_type == 'bot' else outputs)[low_id].append(low_value)
                (bots if high_type == 'bot' else outputs)[high_id].append(high_value)
                bots[bot] = []
                instructions_to_execute.remove(instruction)
    part2 = outputs[0][0] * outputs[1][0] * outputs[2][0]
    return part1, part2

instructions = read_instructions('10.txt')

# Part 1
part1, _ = execute_instructions(instructions)
print(part1)

# Part 2
_, part2 = execute_instructions(instructions)
print(part2)