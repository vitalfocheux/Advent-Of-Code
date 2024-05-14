'''
Un essai pour résoudre le jour 17 de l'Avent Of Code 2017
'''
def spinlock(steps, rounds):
    buffer = [0]
    pos = 0
    for i in range(1, rounds + 1):
        pos = (pos + steps) % i + 1
        buffer.insert(pos, i)
    return buffer

# Partie 1
steps = 382
buffer = spinlock(steps, 2017)
index_2017 = buffer.index(2017)
print(buffer[(index_2017 + 1) % len(buffer)])

# Partie 2
pos = 0
result = None
for i in range(1, 50000001):
    pos = (pos + steps) % i + 1
    if pos == 1:
        result = i
print(result)