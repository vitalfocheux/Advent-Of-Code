'''
Un essai pour résoudre le jour 11 de l'année 2015
'''
import re

def increment_password(password):
    password = list(password)
    for i in range(len(password) - 1, -1, -1):
        if password[i] == 'z':
            password[i] = 'a'
        else:
            password[i] = chr(ord(password[i]) + 1)
            break
    return ''.join(password)

def is_valid_password(password):
    if any(letter in password for letter in 'iol'):
        return False
    if len(re.findall(r'(.)\1', password)) < 2:
        return False
    for i in range(len(password) - 2):
        if ord(password[i]) + 1 == ord(password[i+1]) == ord(password[i+2]) - 1:
            return True
    return False

def next_valid_password(password):
    password = increment_password(password)
    while not is_valid_password(password):
        password = increment_password(password)
    return password

with open('11.txt', 'r') as file:
    password = file.read().strip()

# Part 1
password = next_valid_password(password)
print(password)

# Part 2
password = next_valid_password(password)
print(password)