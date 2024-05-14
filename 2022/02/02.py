'''
Un essai avec Llama3-70b-8192 pour résoudre le jour 2 de 2022
'''

def calculate_score(strategy_guide):
    score = 0
    shape_scores = {'X': 1, 'Y': 2, 'Z': 3}
    outcome_scores = {'win': 6, 'loss': 0, 'draw': 3}

    for line in strategy_guide:
        opponent, me = line.strip().split()
        opponent_shape = {'A': 'Rock', 'B': 'Paper', 'C': 'Scissors'}[opponent]
        my_shape = {'X': 'Rock', 'Y': 'Paper', 'Z': 'Scissors'}[me]

        if opponent_shape == my_shape:
            outcome = 'draw'
        elif (opponent_shape == 'Rock' and my_shape == 'Paper') or \
             (opponent_shape == 'Paper' and my_shape == 'Scissors') or \
             (opponent_shape == 'Scissors' and my_shape == 'Rock'):
            outcome = 'win'
        else:
            outcome = 'loss'

        score += shape_scores[me] + outcome_scores[outcome]

    return score

with open('02.txt', 'r') as f:
    strategy_guide = f.readlines()

print(calculate_score(strategy_guide))


def calculate_score(strategy_guide):
    score = 0
    shape_scores = {'Rock': 1, 'Paper': 2, 'Scissors': 3}
    outcome_scores = {'win': 6, 'loss': 0, 'draw': 3}

    for line in strategy_guide:
        opponent, outcome = line.strip().split()
        opponent_shape = {'A': 'Rock', 'B': 'Paper', 'C': 'Scissors'}[opponent]
        if outcome == 'X':  # lose
            my_shape = {'Rock': 'Scissors', 'Paper': 'Rock', 'Scissors': 'Paper'}[opponent_shape]
        elif outcome == 'Y':  # draw
            my_shape = opponent_shape
        else:  # win
            my_shape = {'Rock': 'Paper', 'Paper': 'Scissors', 'Scissors': 'Rock'}[opponent_shape]

        score += shape_scores[my_shape]
        if opponent_shape == my_shape:
            score += outcome_scores['draw']
        elif (opponent_shape == 'Rock' and my_shape == 'Paper') or \
             (opponent_shape == 'Paper' and my_shape == 'Scissors') or \
             (opponent_shape == 'Scissors' and my_shape == 'Rock'):
            score += outcome_scores['win']
        else:
            score += outcome_scores['loss']

    return score

with open('02.txt', 'r') as f:
    strategy_guide = f.readlines()

print(calculate_score(strategy_guide))