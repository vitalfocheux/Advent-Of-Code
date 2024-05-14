'''
Un essai pour résoudre le jour 4 de l'année 2020.
'''
import re

REQUIRED_FIELDS = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}
VALID_EYE_COLORS = {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'}

def is_valid_part1(passport):
    return REQUIRED_FIELDS.issubset(passport.keys())

def is_valid_part2(passport):
    if not is_valid_part1(passport):
        return False

    if not (1920 <= int(passport['byr']) <= 2002):
        return False
    if not (2010 <= int(passport['iyr']) <= 2020):
        return False
    if not (2020 <= int(passport['eyr']) <= 2030):
        return False

    height = re.fullmatch(r'(\d+)(cm|in)', passport['hgt'])
    if height is None:
        return False
    if height.group(2) == 'cm' and not (150 <= int(height.group(1)) <= 193):
        return False
    if height.group(2) == 'in' and not (59 <= int(height.group(1)) <= 76):
        return False

    if not re.fullmatch(r'#[0-9a-f]{6}', passport['hcl']):
        return False
    if passport['ecl'] not in VALID_EYE_COLORS:
        return False
    if not re.fullmatch(r'\d{9}', passport['pid']):
        return False

    return True

def main():
    with open('04.txt', 'r') as file:
        passports = file.read().split('\n\n')

    valid_part1 = 0
    valid_part2 = 0
    for passport in passports:
        fields = dict(field.split(':') for field in re.findall(r'\b(\w+:\S+)', passport))
        if is_valid_part1(fields):
            valid_part1 += 1
        if is_valid_part2(fields):
            valid_part2 += 1

    print(valid_part1)
    print(valid_part2)

if __name__ == "__main__":
    main()