'''
Un essai pour résoudre le jour 4 de l'année 2019
'''
def parse_input(input_lines):
    return list(map(int, input_lines[0].split('-')))

def is_valid_password(password, part2=False):
    digits = list(map(int, str(password)))
    has_double = False
    for i in range(1, len(digits)):
        if digits[i] < digits[i-1]:
            return False
        if digits[i] == digits[i-1]:
            if part2:
                if (i == 1 or digits[i-2] != digits[i]) and (i == len(digits) - 1 or digits[i+1] != digits[i]):
                    has_double = True
            else:
                has_double = True
    return has_double

def part1(input_lines):
    start, end = parse_input(input_lines)
    return sum(is_valid_password(password) for password in range(start, end+1))

def part2(input_lines):
    start, end = parse_input(input_lines)
    return sum(is_valid_password(password, True) for password in range(start, end+1))

# Test the program with your input
with open('04.txt') as f:
    input_lines = f.readlines()
print(part1(input_lines))  # Part 1
print(part2(input_lines))  # Part 2