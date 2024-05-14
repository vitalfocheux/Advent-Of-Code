'''
Un essai pour résoudre la partie 1
N'a pas réussi pour la partie 2 au bout de 10 essais
'''
import re
from collections import defaultdict

def parse_input(input):
    children = defaultdict(list)
    weights = {}
    for line in input.split('\n'):
        name, weight, *c = re.findall(r'\w+', line)
        weights[name] = int(weight)
        children[name] = c
    return children, weights

def solve_part1(input):
    children, weights = parse_input(input)
    return (set(weights.keys()) - set(c for cs in children.values() for c in cs)).pop()

def find_root(children, weights):
    return (set(weights.keys()) - set(c for cs in children.values() for c in cs)).pop()

def total_weight(name, children, weights):
    return weights[name] + sum(total_weight(c, children, weights) for c in children[name])

def find_imbalance(name, children, weights):
    child_weights = [total_weight(c, children, weights) for c in children[name]]
    if len(set(child_weights)) > 1:
        correct_weight = max(set(child_weights), key=child_weights.count)
        wrong_weight = min(set(child_weights), key=child_weights.count)
        wrong_child = children[name][child_weights.index(wrong_weight)]
        diff = correct_weight - wrong_weight
        return weights[wrong_child] + diff
    for child in children[name]:
        imbalance = find_imbalance(child, children, weights)
        if imbalance:
            return imbalance

def solve_part2(input):
    children, weights = parse_input(input)
    root = find_root(children, weights)
    return find_imbalance(root, children, weights)

input = open('07.txt').read()

# Partie 1
print(solve_part1(input.strip()))

# Partie 2
print(solve_part2(input.strip()))