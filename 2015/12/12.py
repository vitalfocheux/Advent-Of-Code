import json

def sum_numbers(data):
    if isinstance(data, int):
        return data
    if isinstance(data, list):
        return sum(sum_numbers(item) for item in data)
    if isinstance(data, dict):
        return sum(sum_numbers(item) for item in data.values())
    return 0

def sum_numbers_ignore_red(data):
    if isinstance(data, int):
        return data
    if isinstance(data, list):
        return sum(sum_numbers_ignore_red(item) for item in data)
    if isinstance(data, dict):
        if "red" in data.values():
            return 0
        return sum(sum_numbers_ignore_red(item) for item in data.values())
    return 0

with open('12.txt', 'r') as file:
    data = json.load(file)

# Part 1
print(sum_numbers(data))

# Part 2
print(sum_numbers_ignore_red(data))