'''
Un essai pour résoudre le jour 19 de 2017
'''
def solve(input):
    diagram = input.splitlines()
    direction = (1, 0)
    position = (0, diagram[0].index('|'))
    letters = []
    steps = 0

    while True:
        steps += 1
        position = (position[0] + direction[0], position[1] + direction[1])
        c = diagram[position[0]][position[1]]

        if c == '+':
            if direction[0] == 0:
                if diagram[position[0] + 1][position[1]] != ' ':
                    direction = (1, 0)
                else:
                    direction = (-1, 0)
            else:
                if diagram[position[0]][position[1] + 1] != ' ':
                    direction = (0, 1)
                else:
                    direction = (0, -1)
        elif c == ' ':
            break
        elif c not in '-|':
            letters.append(c)

    return ''.join(letters), steps

input = open('19.txt').read()
print(solve(input))  # Part 1 and 2