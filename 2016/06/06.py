'''
Un essai pour résoudre le problème 06 de Advent of Code 2016
'''
from collections import Counter

def read_messages(file_path):
    with open(file_path, 'r') as file:
        return file.read().splitlines()

def decode_message(messages, most_common):
    return ''.join(Counter(column).most_common()[most_common][0] for column in zip(*messages))

messages = read_messages('06.txt')

# Part 1
print(decode_message(messages, 0))

# Part 2
print(decode_message(messages, -1))