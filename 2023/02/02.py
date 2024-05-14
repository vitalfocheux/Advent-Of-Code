'''
Un essai pour la partie 1
La partie 2 ne fonctionne pas
'''
def possible_games(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()

    sum_of_ids = 0
    for line in lines:
        game_id, rounds = line.split(':')
        game_id = int(game_id.split()[1])
        rounds = rounds.split(';')

        possible = True
        for round in rounds:
            colors = round.split(',')
            for color in colors:
                count, color = color.split()
                if (color.strip() == 'red' and int(count) > 12) or \
                   (color.strip() == 'green' and int(count) > 13) or \
                   (color.strip() == 'blue' and int(count) > 14):
                    possible = False
                    break
            if not possible:
                break

        if possible:
            sum_of_ids += game_id

    return sum_of_ids

print(possible_games('02.txt'))