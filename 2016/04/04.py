'''
Un essai pour résoudre le problème du jour 4.
'''
import re
from collections import Counter

def read_rooms(file_path):
    with open(file_path, 'r') as file:
        return file.read().splitlines()

def parse_room(room):
    match = re.match(r'([a-z\-]+)-(\d+)\[([a-z]+)\]', room)
    return match.groups()

def calculate_checksum(name):
    counter = Counter(name.replace('-', ''))
    return ''.join(sorted(counter, key=lambda x: (-counter[x], x))[:5])

def is_real_room(room):
    name, sector_id, checksum = parse_room(room)
    return calculate_checksum(name) == checksum

def decrypt_name(name, sector_id):
    decrypted = ''
    for char in name:
        if char == '-':
            decrypted += ' '
        else:
            decrypted += chr((ord(char) - ord('a') + int(sector_id)) % 26 + ord('a'))
    return decrypted

rooms = read_rooms('04.txt')

# Part 1
real_rooms = [room for room in rooms if is_real_room(room)]
print(sum(int(parse_room(room)[1]) for room in real_rooms))

# Part 2
for room in real_rooms:
    name, sector_id, _ = parse_room(room)
    decrypted_name = decrypt_name(name, sector_id)
    if 'north' in decrypted_name:
        print(sector_id)
        break