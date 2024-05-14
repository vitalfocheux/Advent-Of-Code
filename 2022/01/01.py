'''
Un essai pour résoudre le jour 1 de l'année 2022
'''
def solve():
    with open('01.txt') as f:
        elves = f.read().split('\n\n')

    totals = [sum(map(int, elf.split())) for elf in elves]
    totals.sort(reverse=True)

    most_calories = totals[0]
    top_three_calories = sum(totals[:3])

    return most_calories, top_three_calories

print(solve())