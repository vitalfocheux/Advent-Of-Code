'''
Un essai pour la partie 1 avec Llama3-70b-8192
'''
def scramble_password(password, operations):
    for op in operations:
        words = op.split()
        if words[0] == 'swap' and words[1] == 'position':
            x, y = int(words[2]), int(words[5])
            password = list(password)
            password[x], password[y] = password[y], password[x]
            password = ''.join(password)
        elif words[0] == 'swap' and words[1] == 'letter':
            x, y = words[2], words[5]
            password = password.replace(x, '#').replace(y, x).replace('#', y)
        elif words[0] == 'rotate' and words[1] == 'left':
            x = int(words[2])
            password = password[x:] + password[:x]
        elif words[0] == 'rotate' and words[1] == 'right':
            x = int(words[2])
            password = password[-x:] + password[:-x]
        elif words[0] == 'rotate' and words[1] == 'based':
            x = words[6]
            idx = password.index(x)
            password = list(password)
            password = password[-1:] + password[:-1]
            for _ in range(idx):
                password = password[-1:] + password[:-1]
            if idx >= 4:
                password = password[-1:] + password[:-1]
            password = ''.join(password)
        elif words[0] == 'reverse':
            x, y = int(words[2]), int(words[4])
            password = list(password)
            password[x:y+1] = password[x:y+1][::-1]
            password = ''.join(password)
        elif words[0] == 'move':
            x, y = int(words[2]), int(words[5])
            password = list(password)
            c = password.pop(x)
            password.insert(y, c)
            password = ''.join(password)
    return password

with open('21.txt', 'r') as f:
    operations = [line.strip() for line in f.readlines()]

password = 'abcdefgh'
print(scramble_password(password, operations))

