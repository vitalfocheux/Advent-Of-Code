'''
Un essai pour résoudre le jour 11 de l'année 2020.
'''
def count_occupied(seats):
    return sum(row.count('#') for row in seats)

def get_adjacent(seats, row, col):
    return [seats[r][c] for r in range(max(0, row - 1), min(len(seats), row + 2))
            for c in range(max(0, col - 1), min(len(seats[0]), col + 2)) if (r, c) != (row, col)]

def get_visible(seats, row, col):
    directions = [(dr, dc) for dr in range(-1, 2) for dc in range(-1, 2) if (dr, dc) != (0, 0)]
    visible = []
    for dr, dc in directions:
        r, c = row + dr, col + dc
        while 0 <= r < len(seats) and 0 <= c < len(seats[0]):
            if seats[r][c] != '.':
                visible.append(seats[r][c])
                break
            r, c = r + dr, c + dc
    return visible

def simulate(seats, get_neighbors, tolerance):
    while True:
        new_seats = [list(row) for row in seats]
        for r in range(len(seats)):
            for c in range(len(seats[0])):
                neighbors = get_neighbors(seats, r, c)
                if seats[r][c] == 'L' and neighbors.count('#') == 0:
                    new_seats[r][c] = '#'
                elif seats[r][c] == '#' and neighbors.count('#') >= tolerance:
                    new_seats[r][c] = 'L'
        if new_seats == seats:
            return count_occupied(seats)
        seats = new_seats

def main():
    with open('11.txt', 'r') as file:
        seats = [list(line.strip()) for line in file]

    print(simulate(seats, get_adjacent, 4))
    print(simulate(seats, get_visible, 5))

if __name__ == "__main__":
    main()