'''
Deux essais pour la partie 1
Trois essais pour la partie 2
'''
import re

def parse_rules_and_messages(input):
    rules, messages = input.strip().split("\n\n")
    rules = dict(rule.split(": ") for rule in rules.split("\n"))
    messages = messages.split("\n")
    return rules, messages

def build_regex(rules, rule_number="0", depth=0):
    rule = rules[rule_number]
    if depth > 20:  # Limite arbitraire pour éviter une récursion infinie
        return ""
    if rule == '"a"' or rule == '"b"':
        return rule[1]
    elif "|" in rule:
        sub_rules = rule.split(" | ")
        return "(" + "|".join("".join(build_regex(rules, sub_rule, depth+1) for sub_rule in sub_rule_group.split()) for sub_rule_group in sub_rules) + ")"
    else:
        return "".join(build_regex(rules, sub_rule, depth+1) for sub_rule in rule.split())

def count_valid_messages(rules, messages):
    regex = re.compile("^" + build_regex(rules) + "$")
    return sum(1 for message in messages if regex.match(message))

def solve_part1(input):
    rules, messages = parse_rules_and_messages(input)
    return count_valid_messages(rules, messages)

def solve_part2(input):
    rules, messages = parse_rules_and_messages(input)
    rules["8"] = "42 | 42 8"
    rules["11"] = "42 31 | 42 11 31"
    return count_valid_messages(rules, messages)

def main():
    with open('19.txt', 'r') as file:
        input = file.read()

    print(solve_part1(input))
    print(solve_part2(input))

if __name__ == "__main__":
    main()