'''
Trois essais pour la partie 1
Pas la foi d'attendre 20 minutes pour la partie 2
'''
import re
from copy import deepcopy

def parse_input(input_lines):
    def parse_group(line):
        nums = list(map(int, re.findall(r'\d+', line)))
        dmg_type = re.search(r'(\w+) damage', line).group(1)
        weaknesses = re.search(r'weak to ([\w, ]+)', line)
        weaknesses = set(weaknesses.group(1).split(', ')) if weaknesses else set()
        immunities = re.search(r'immune to ([\w, ]+)', line)
        immunities = set(immunities.group(1).split(', ')) if immunities else set()
        return {'units': nums[0], 'hp': nums[1], 'dmg': nums[2], 'initiative': nums[3], 'dmg_type': dmg_type, 'weak': weaknesses, 'immune': immunities}

    lines = iter(input_lines)
    next(lines)  # Skip "Immune System:"
    immune_system = []
    while line := next(lines).strip():
        immune_system.append(parse_group(line))
    next(lines)  # Skip "Infection:"
    infection = []
    while line := next(lines, '').strip():
        infection.append(parse_group(line))
    return immune_system, infection

def simulate_battle(immune_system, infection):
    while immune_system and infection:
        total_units = sum(g['units'] for g in immune_system + infection)
        # Target selection
        for army in (immune_system, infection):
            for group in sorted(army, key=lambda g: (-g['units'] * g['dmg'], -g['initiative'])):
                enemies = (infection if group in immune_system else immune_system)
                group['target'] = max((e for e in enemies if 'targeted' not in e), key=lambda e: (calc_damage(group, e), e['units'] * e['dmg'], e['initiative']), default=None)
                if group['target']:
                    group['target']['targeted'] = True
        # Attacking
        for group in sorted(immune_system + infection, key=lambda g: -g['initiative']):
            if group['units'] > 0 and 'target' in group and group['target'] is not None and group['target']['units'] > 0:
                dmg = calc_damage(group, group['target'])
                killed = min(group['target']['units'], dmg // group['target']['hp'])
                group['target']['units'] -= killed
        # Cleanup
        immune_system = [g for g in immune_system if g['units'] > 0]
        infection = [g for g in infection if g['units'] > 0]
        for group in immune_system + infection:
            group.pop('target', None)
            group.pop('targeted', None)
        # Check if any damage was done
        if total_units == sum(g['units'] for g in immune_system + infection):
            return None  # No damage was done, stop the simulation
    return sum(g['units'] for g in immune_system + infection)

def calc_damage(attacker, defender):
    if attacker['dmg_type'] in defender['immune']:
        return 0
    elif attacker['dmg_type'] in defender['weak']:
        return 2 * attacker['units'] * attacker['dmg']
    else:
        return attacker['units'] * attacker['dmg']

def part1(input_lines):
    immune_system, infection = parse_input(input_lines)
    return simulate_battle(deepcopy(immune_system), deepcopy(infection))

def part2(input_lines):
    immune_system, infection = parse_input(input_lines)
    boost = 0
    while True:
        boost += 1
        for group in immune_system:
            group['dmg'] += 1
        result = simulate_battle(deepcopy(immune_system), deepcopy(infection))
        if result is not None and result == sum(g['units'] for g in immune_system):
            return boost


# Test the program with your input
with open('24.txt') as f:
    input_lines = f.readlines()
print(part1(input_lines))  # Part 1
print(part2(input_lines))  # Part 2