'''
Un essai pour résoudre le jour 21 du calendrier de l'avent 2020
'''
from collections import defaultdict

def parse_input(input):
    foods = []
    for line in input.strip().split('\n'):
        ingredients, allergens = line[:-1].split(' (contains ')
        foods.append((set(ingredients.split()), set(allergens.split(', '))))
    return foods

def solve(input):
    foods = parse_input(input)
    possible_allergens = defaultdict(set)
    for ingredients, allergens in foods:
        for allergen in allergens:
            if allergen in possible_allergens:
                possible_allergens[allergen] &= ingredients
            else:
                possible_allergens[allergen] = ingredients.copy()
    allergen_ingredients = {}
    while possible_allergens:
        allergen, ingredients = min(possible_allergens.items(), key=lambda x: len(x[1]))
        ingredient = ingredients.pop()
        allergen_ingredients[allergen] = ingredient
        del possible_allergens[allergen]
        for ingredients in possible_allergens.values():
            ingredients.discard(ingredient)
    safe_ingredients = set(ingredient for ingredients, _ in foods for ingredient in ingredients) - set(allergen_ingredients.values())
    part1 = sum(ingredient in safe_ingredients for ingredients, _ in foods for ingredient in ingredients)
    part2 = ','.join(ingredient for allergen, ingredient in sorted(allergen_ingredients.items()))
    return part1, part2

input = open('21.txt').read()

print(solve(input))