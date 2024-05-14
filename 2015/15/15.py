'''
Trois essais pour résoudre le jour 15 de l'année 2015
'''
import re
from itertools import product

def read_ingredients(file_path):
    ingredients = []
    with open(file_path, 'r') as file:
        for line in file:
            _, capacity, durability, flavor, texture, calories = re.match(r'(\w+): capacity (-?\d+), durability (-?\d+), flavor (-?\d+), texture (-?\d+), calories (-?\d+)', line).groups()
            ingredients.append([int(capacity), int(durability), int(flavor), int(texture), int(calories)])
    return ingredients

def calculate_score(ingredients, amounts, include_calories=False):
    properties = [0] * 5
    for ingredient, amount in zip(ingredients, amounts):
        for i in range(5):
            properties[i] += ingredient[i] * amount
    if include_calories and properties[4] != 500:
        return 0
    return max(0, properties[0]) * max(0, properties[1]) * max(0, properties[2]) * max(0, properties[3])

ingredients = read_ingredients('15.txt')

# Generate all combinations of amounts that sum to 100
amounts = [seq for seq in product(range(101), repeat=len(ingredients)) if sum(seq) == 100]

# Part 1
print(max(calculate_score(ingredients, amount) for amount in amounts))

# Part 2
print(max(calculate_score(ingredients, amount, True) for amount in amounts))