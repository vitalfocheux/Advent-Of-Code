'''
Un essai avec Llama3-70b-8192 pour résoudre le jour 9 de 2022
'''
def simulate_rope(motions):
    head_x, head_y = 0, 0
    tail_x, tail_y = 0, 0
    tail_positions = set([(0, 0)])

    for motion in motions:
        direction, steps = motion.split()
        steps = int(steps)

        for _ in range(steps):
            if direction == 'R':
                head_x += 1
            elif direction == 'L':
                head_x -= 1
            elif direction == 'U':
                head_y += 1
            elif direction == 'D':
                head_y -= 1

            dx = head_x - tail_x
            dy = head_y - tail_y

            if abs(dx) > 1 or abs(dy) > 1:
                if dx != 0:
                    tail_x += dx // abs(dx)
                if dy != 0:
                    tail_y += dy // abs(dy)

            tail_positions.add((tail_x, tail_y))

    return len(tail_positions)

with open('09.txt', 'r') as f:
    motions = [line.strip() for line in f.readlines()]

print(simulate_rope(motions))

def simulate_rope(motions):
    knots = [(0, 0) for _ in range(10)]
    tail_positions = set([(0, 0)])

    for motion in motions:
        direction, steps = motion.split()
        steps = int(steps)

        for _ in range(steps):
            if direction == 'R':
                knots[0] = (knots[0][0] + 1, knots[0][1])
            elif direction == 'L':
                knots[0] = (knots[0][0] - 1, knots[0][1])
            elif direction == 'U':
                knots[0] = (knots[0][0], knots[0][1] + 1)
            elif direction == 'D':
                knots[0] = (knots[0][0], knots[0][1] - 1)

            for i in range(1, 10):
                dx = knots[i-1][0] - knots[i][0]
                dy = knots[i-1][1] - knots[i][1]

                if abs(dx) > 1 or abs(dy) > 1:
                    if dx != 0:
                        knots[i] = (knots[i][0] + dx // abs(dx), knots[i][1])
                    if dy != 0:
                        knots[i] = (knots[i][0], knots[i][1] + dy // abs(dy))

            tail_positions.add(knots[-1])

    return len(tail_positions)

with open('09.txt', 'r') as f:
    motions = [line.strip() for line in f.readlines()]

print(simulate_rope(motions))