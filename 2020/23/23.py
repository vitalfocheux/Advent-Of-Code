'''
Un essai pour résoudre le jour 23 du calendrier de l'avent 2020
'''
def play_game(cups, rounds):
    max_cup = max(cups)
    min_cup = min(cups)
    current_cup = cups[0]
    next_cups = {cup: cups[i + 1] if i + 1 < len(cups) else cups[0] for i, cup in enumerate(cups)}
    for _ in range(rounds):
        picked_up = [next_cups[current_cup]]
        for _ in range(2):
            picked_up.append(next_cups[picked_up[-1]])
        next_cups[current_cup] = next_cups[picked_up[-1]]
        destination_cup = current_cup - 1 if current_cup > min_cup else max_cup
        while destination_cup in picked_up:
            destination_cup = destination_cup - 1 if destination_cup > min_cup else max_cup
        next_cups[picked_up[-1]] = next_cups[destination_cup]
        next_cups[destination_cup] = picked_up[0]
        current_cup = next_cups[current_cup]
    return next_cups

def solve(input, rounds1, rounds2):
    cups = list(map(int, input.strip()))
    next_cups = play_game(cups, rounds1)
    cup = next_cups[1]
    part1 = ''
    while cup != 1:
        part1 += str(cup)
        cup = next_cups[cup]
    cups += list(range(max(cups) + 1, 1000001))
    next_cups = play_game(cups, rounds2)
    part2 = next_cups[1] * next_cups[next_cups[1]]
    return part1, part2

input = "247819356"
print(solve(input, 100, 10000000))