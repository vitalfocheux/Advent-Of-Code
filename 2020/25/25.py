'''
Un essai pour résoudre le jour 25 du calendrier de l'avent 2020
'''
def transform(subject_number, loop_size):
    value = 1
    for _ in range(loop_size):
        value = (value * subject_number) % 20201227
    return value

def find_loop_size(public_key):
    value = 1
    loop_size = 0
    while value != public_key:
        value = (value * 7) % 20201227
        loop_size += 1
    return loop_size

def solve(input):
    card_public_key, door_public_key = map(int, input.strip().split('\n'))
    card_loop_size = find_loop_size(card_public_key)
    door_loop_size = find_loop_size(door_public_key)
    encryption_key = transform(door_public_key, card_loop_size)
    return encryption_key, "Congratulations on completing Advent of Code 2020!"

input = open('25.txt').read()

print(solve(input))