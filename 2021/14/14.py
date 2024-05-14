'''
Un essai pour la partie 1
La partie 2 ne fonctionne pas
'''
from collections import Counter

def polymer_insertion(template, rules, steps=10):
    # Repeat the pair insertion process 10 times
    for _ in range(steps):
        new_template = ''
        for i in range(len(template) - 1):
            pair = template[i:i+2]
            new_template += pair[0] + rules[pair]
        new_template += template[-1]
        template = new_template

    # Count the occurrences of each element
    counts = Counter(template)

    # Find the most common and least common elements
    most_common = counts.most_common(1)[0][1]
    least_common = counts.most_common()[-1][1]

    return most_common - least_common

# Convert input to polymer template and pair insertion rules
input = open('14.txt').read().splitlines()
template = input[0]
rules = {}
for rule in input[2:]:
    key, value = rule.split(' -> ')
    rules[key] = value
print(polymer_insertion(template, rules))