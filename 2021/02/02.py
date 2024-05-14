def solve(data, is_part2=False):
    directions = {
        'down': (0, -1, 0),
        'up': (0, 1, 0),
    }
    if is_part2:
        directions.update({
            'north': (0, 0, -1),
            'south': (0, 0, 1),
            'east': (1, 0, 0),
            'west': (-1, 0, 0),
        })
    else:
        directions['forward'] = (1, 0, 0)

    position = [0, 0, 0]
    orientation = [1, 0, 0]
    for line in data:
        action, value = line.split()
        value = int(value)
        if action == 'forward':
            dx, dy, dz = orientation
        else:
            dx, dy, dz = directions[action]
            if is_part2 and action in ('north', 'south', 'east', 'west'):
                orientation = [dx, dy, dz]
        position[0] += dx * value
        position[1] += dy * value
        position[2] += dz * value

    return abs(position[0]) + abs(position[1]) + abs(position[2])

def main():
    with open('02.txt', 'r') as file:
        data = file.read().splitlines()
    print(f"Part 1: {solve(data)}")
    print(f"Part 2: {solve(data, is_part2=True)}")

if __name__ == "__main__":
    main()