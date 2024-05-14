'''
Un essai pour résoudre le jour 14 de l'année 2018
'''
def solve_part1(input):
    recipes = [3, 7]
    elf1, elf2 = 0, 1
    while len(recipes) < input + 10:
        total = recipes[elf1] + recipes[elf2]
        recipes.extend(divmod(total, 10) if total >= 10 else (total,))
        elf1 = (elf1 + 1 + recipes[elf1]) % len(recipes)
        elf2 = (elf2 + 1 + recipes[elf2]) % len(recipes)
    return ''.join(map(str, recipes[input:input+10]))

def solve_part2(input):
    recipes = [3, 7]
    elf1, elf2 = 0, 1
    input = list(map(int, str(input)))
    len_input = len(input)
    while recipes[-len_input:] != input and recipes[-len_input-1:-1] != input:
        total = recipes[elf1] + recipes[elf2]
        recipes.extend(divmod(total, 10) if total >= 10 else (total,))
        elf1 = (elf1 + 1 + recipes[elf1]) % len(recipes)
        elf2 = (elf2 + 1 + recipes[elf2]) % len(recipes)
    return len(recipes) - len_input - (0 if recipes[-len_input:] == input else 1)

input = 330121
print(solve_part1(input))  # solution for part 1
print(solve_part2(input))  # solution for part 2