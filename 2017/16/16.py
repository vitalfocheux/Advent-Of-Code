'''
Un essai pour la partie 1
Sept essais pour la partie 2
'''
def dance(programs, moves):
    for move in moves:
        if move[0] == 's':
            size = int(move[1:])
            programs = programs[-size:] + programs[:-size]
        elif move[0] == 'x':
            posA, posB = map(int, move[1:].split('/'))
            programs[posA], programs[posB] = programs[posB], programs[posA]
        elif move[0] == 'p':
            progA, progB = move[1:].split('/')
            posA, posB = programs.index(progA), programs.index(progB)
            programs[posA], programs[posB] = programs[posB], programs[posA]
    return programs

def solve(programs, moves, rounds):
    seen = {"".join(programs): 0}
    for i in range(1, rounds+1):
        programs = dance(programs, moves)
        key = "".join(programs)
        if key in seen:
            cycle_length = i - seen[key]
            remaining = (rounds - seen[key]) % cycle_length
            for cycle_key, cycle_value in seen.items():
                if cycle_value == seen[key] + remaining:
                    return cycle_key
        seen[key] = i
    return "".join(programs)

programs = list('abcdefghijklmnop')
moves = open('16.txt').read().strip().split(',')

# Partie 1
print(solve(programs[:], moves, 1))

# Partie 2
print(solve(programs[:], moves, 1000000000))