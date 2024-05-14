'''
Un essai pour résoudre le jour 12 de l'année 2020.
'''
def move_ship(instructions):
    x, y, dx, dy = 0, 0, 1, 0
    for action, value in instructions:
        if action == 'N':
            y += value
        elif action == 'S':
            y -= value
        elif action == 'E':
            x += value
        elif action == 'W':
            x -= value
        elif action == 'L':
            for _ in range(value // 90):
                dx, dy = -dy, dx
        elif action == 'R':
            for _ in range(value // 90):
                dx, dy = dy, -dx
        elif action == 'F':
            x += dx * value
            y += dy * value
    return abs(x) + abs(y)

def move_waypoint(instructions):
    x, y, dx, dy = 0, 0, 10, 1
    for action, value in instructions:
        if action == 'N':
            dy += value
        elif action == 'S':
            dy -= value
        elif action == 'E':
            dx += value
        elif action == 'W':
            dx -= value
        elif action == 'L':
            for _ in range(value // 90):
                dx, dy = -dy, dx
        elif action == 'R':
            for _ in range(value // 90):
                dx, dy = dy, -dx
        elif action == 'F':
            x += dx * value
            y += dy * value
    return abs(x) + abs(y)

def main():
    with open('12.txt', 'r') as file:
        instructions = [(line[0], int(line[1:].strip())) for line in file]

    print(move_ship(instructions))
    print(move_waypoint(instructions))

if __name__ == "__main__":
    main()