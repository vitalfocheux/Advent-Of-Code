'''
Un essai pour résoudre le jour 5 de l'année 2015
'''
import re

def read_strings(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file]

def part1(strings):
    vowels = 'aeiou'
    forbidden = ['ab', 'cd', 'pq', 'xy']
    count = 0
    for s in strings:
        if any(f in s for f in forbidden):
            continue
        if sum(s.count(v) for v in vowels) < 3:
            continue
        if not any(s[i] == s[i+1] for i in range(len(s) - 1)):
            continue
        count += 1
    return count

def part2(strings):
    count = 0
    for s in strings:
        if not re.search(r'(..).*\1', s):
            continue
        if not re.search(r'(.).\1', s):
            continue
        count += 1
    return count

strings = read_strings('05.txt')

# Part 1
print(part1(strings))

# Part 2
print(part2(strings))