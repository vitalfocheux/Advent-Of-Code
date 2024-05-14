'''
Un essai pour résoudre le jour 9 de l'année 2018
'''
from collections import deque, defaultdict

def play_game(max_players, last_marble):
    scores = defaultdict(int)
    circle = deque([0])

    for marble in range(1, last_marble + 1):
        if marble % 23 == 0:
            circle.rotate(7)
            scores[marble % max_players] += marble + circle.pop()
            circle.rotate(-1)
        else:
            circle.rotate(-1)
            circle.append(marble)

    return max(scores.values()) if scores else 0

# Replace with your input
max_players = 455
last_marble = 71223

print(f"Part 1: {play_game(max_players, last_marble)}")
print(f"Part 2: {play_game(max_players, last_marble * 100)}")