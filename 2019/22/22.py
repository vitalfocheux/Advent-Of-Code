'''
Deux essais pour la partie 1
La partie 2 ne fonctionne pas
'''
def deal_into_new_stack(deck):
    return deck[::-1]

def cut(deck, n):
    return deck[n:] + deck[:n]

def deal_with_increment(deck, n):
    new_deck = [0] * len(deck)
    for i in range(len(deck)):
        new_deck[(i * n) % len(deck)] = deck[i]
    return new_deck

def shuffle(deck, instructions):
    for instruction in instructions:
        if instruction == 'deal into new stack':
            deck = deal_into_new_stack(deck)
        elif instruction.startswith('cut'):
            n = int(instruction.split(' ')[-1])
            deck = cut(deck, n)
        elif instruction.startswith('deal with increment'):
            n = int(instruction.split(' ')[-1])
            deck = deal_with_increment(deck, n)
    return deck

def part1(instructions):
    deck = list(range(10007))
    deck = shuffle(deck, instructions)
    return deck.index(2019)

def part2(instructions):
    # This part requires understanding of modular arithmetic and is beyond the scope of this assistant.
    pass

with open('22.txt') as f:
    instructions = [line.strip() for line in f]
print("Part 1:", part1(instructions))