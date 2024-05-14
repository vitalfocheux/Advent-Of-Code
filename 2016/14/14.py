'''
Deux essais pour résoudre le jour 14 de l'Avent de Code 2016
'''
import hashlib
import re

def generate_hash(salt, index, part2):
    to_hash = (salt + str(index)).encode('utf-8')
    result_hash = hashlib.md5(to_hash).hexdigest()
    if part2:
        for _ in range(2016):
            result_hash = hashlib.md5(result_hash.encode('utf-8')).hexdigest()
    return result_hash

def find_keys(salt, part2=False):
    index = 0
    keys = []
    potential_keys = {}
    while len(keys) < 64 or index - keys[-1][1] < 1000:
        current_hash = generate_hash(salt, index, part2)
        five_in_a_row = re.search(r'(.)\1\1\1\1', current_hash)
        if five_in_a_row:
            char = five_in_a_row.group(1)
            if char in potential_keys:
                for potential_key in potential_keys[char]:
                    if potential_key[1] > index - 1000:
                        keys.append(potential_key)
                del potential_keys[char]
        three_in_a_row = re.search(r'(.)\1\1', current_hash)
        if three_in_a_row:
            char = three_in_a_row.group(1)
            if char not in potential_keys:
                potential_keys[char] = []
            potential_keys[char].append((current_hash, index))
        index += 1
    keys.sort(key=lambda x: x[1])
    return keys[63][1]

# Part 1
print(find_keys('ngcjuoqr'))

# Part 2
print(find_keys('ngcjuoqr', part2=True))