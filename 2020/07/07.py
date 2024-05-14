'''
Quatre essais pour résoudre le jour 7 de l'année 2020.
'''
import re
from collections import defaultdict

def parse_rules(lines):
    rules = defaultdict(dict)
    for line in lines:
        color, contents = re.match(r'(\w+ \w+) bags contain (.+)\.', line).groups()
        if contents != 'no other bags':
            for count, content_color in re.findall(r'(\d+) (\w+ \w+) bags?', contents):
                rules[color][content_color] = int(count)
    return rules

def can_contain_gold(color, rules, memo):
    if color in memo:
        return memo[color]
    memo[color] = 'shiny gold' in rules[color] or any(can_contain_gold(c, rules, memo) for c in rules[color])
    return memo[color]

def count_bags(color, rules):
    return sum(count + count * count_bags(c, rules) for c, count in rules[color].items())

def main():
    with open('07.txt', 'r') as file:
        rules = parse_rules(line.strip() for line in file)

    memo = {}
    colors = list(rules.keys())
    print(sum(can_contain_gold(color, rules, memo) for color in colors))
    print(count_bags('shiny gold', rules))

if __name__ == "__main__":
    main()