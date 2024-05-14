'''
Un essai pour résoudre le jour 14 de l'année 2019 du site Advent of Code
'''
import math
from collections import defaultdict

def parse_input(input):
    reactions = {}
    for line in input.strip().split('\n'):
        inputs, output = line.split(' => ')
        output_qty, output_chem = output.split()
        inputs = [input.split() for input in inputs.split(', ')]
        reactions[output_chem] = (int(output_qty), inputs)
    return reactions

def ore_needed_for_fuel(reactions, fuel_qty):
    needs = defaultdict(int, {'FUEL': fuel_qty})
    leftovers = defaultdict(int)
    while True:
        chem = next((chem for chem, qty in needs.items() if qty > 0 and chem != 'ORE'), None)
        if chem is None: break
        output_qty, inputs = reactions[chem]
        times = math.ceil(needs[chem] / output_qty)
        leftovers[chem] += times * output_qty - needs[chem]
        needs[chem] = 0
        for input_qty, input_chem in inputs:
            needs[input_chem] += times * int(input_qty)
        for chem, qty in leftovers.items():
            if needs[chem] > 0 and leftovers[chem] > 0:
                taken = min(needs[chem], leftovers[chem])
                needs[chem] -= taken
                leftovers[chem] -= taken
    return needs['ORE']

def max_fuel_for_ore(reactions, ore_qty):
    lower = 0
    upper = ore_qty
    while lower < upper:
        mid = (lower + upper + 1) // 2
        if ore_needed_for_fuel(reactions, mid) > ore_qty:
            upper = mid - 1
        else:
            lower = mid
    return lower

input = open('14.txt').read()

reactions = parse_input(input)
print("Part 1:", ore_needed_for_fuel(reactions, 1))
print("Part 2:", max_fuel_for_ore(reactions, 1000000000000))