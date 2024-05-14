'''
Un essai pour la patie 1
La partie 2 ne fonctionne pas
'''
def read_file(filename):
    with open(filename, 'r') as file:
        lines = file.read().splitlines()
    return list(map(int, lines))

def play_game(start_positions):
    scores = [0, 0]
    positions = start_positions
    die = 1
    rolls = 0

    while max(scores) < 1000:
        for i in range(2):
            roll = sum(die + j for j in range(3))
            rolls += 3
            die = (die + 2) % 100 + 1
            positions[i] = (positions[i] + roll - 1) % 10 + 1
            scores[i] += positions[i]
            if scores[i] >= 1000:
                return scores[1 - i] * rolls

start_positions = read_file('21.txt')
result = play_game(start_positions)
print(result)