'''
Un essai pour résoudre le jour 4 de l'année 2015
'''
import hashlib

def read_secret_key(file_path):
    with open(file_path, 'r') as file:
        return file.read().strip()

def part1(secret_key):
    i = 0
    while True:
        to_hash = secret_key + str(i)
        md5_hash = hashlib.md5(to_hash.encode()).hexdigest()
        if md5_hash.startswith('00000'):
            return i
        i += 1

def part2(secret_key):
    i = 0
    while True:
        to_hash = secret_key + str(i)
        md5_hash = hashlib.md5(to_hash.encode()).hexdigest()
        if md5_hash.startswith('000000'):
            return i
        i += 1

secret_key = read_secret_key('04.txt')

# Part 1
print(part1(secret_key))

# Part 2
print(part2(secret_key))