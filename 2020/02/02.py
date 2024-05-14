'''
Un essai pour résoudre le jour 2 de l'année 2020.
'''
import re

def is_valid_part1(min, max, letter, password):
    return min <= password.count(letter) <= max

def is_valid_part2(pos1, pos2, letter, password):
    return (password[pos1-1] == letter) ^ (password[pos2-1] == letter)

def main():
    with open('02.txt', 'r') as file:
        lines = [line.strip() for line in file]

    valid_part1 = 0
    valid_part2 = 0
    for line in lines:
        min, max, letter, password = re.match(r'(\d+)-(\d+) (\w): (\w+)', line).groups()
        min = int(min)
        max = int(max)
        if is_valid_part1(min, max, letter, password):
            valid_part1 += 1
        if is_valid_part2(min, max, letter, password):
            valid_part2 += 1

    print(valid_part1)
    print(valid_part2)

if __name__ == "__main__":
    main()