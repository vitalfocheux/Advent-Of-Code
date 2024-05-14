'''
Un essai pour résoudre le problème du jour 5.
'''
import hashlib

def read_input(file_path):
    with open(file_path, 'r') as file:
        return file.read().strip()

def find_password(door_id):
    password1 = ''
    password2 = [''] * 8
    i = 0
    while len(password1) < 8 or '' in password2:
        hash = hashlib.md5((door_id + str(i)).encode()).hexdigest()
        if hash.startswith('00000'):
            if len(password1) < 8:
                password1 += hash[5]
            if hash[5].isdigit() and int(hash[5]) < 8 and password2[int(hash[5])] == '':
                password2[int(hash[5])] = hash[6]
        i += 1
    return password1, ''.join(password2)

door_id = read_input('05.txt')

# Part 1
password1, _ = find_password(door_id)
print(password1)

# Part 2
_, password2 = find_password(door_id)
print(password2)