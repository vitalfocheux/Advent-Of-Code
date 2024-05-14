'''
Un essai pour résoudre le jour 3 de l'année 2020.
'''
def count_trees(map, right, down):
    rows, cols = len(map), len(map[0])
    row, col = 0, 0
    trees = 0
    while row < rows:
        if map[row][col % cols] == '#':
            trees += 1
        row += down
        col += right
    return trees

def main():
    with open('03.txt', 'r') as file:
        map = [line.strip() for line in file]

    print(count_trees(map, 3, 1))

    slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    product = 1
    for right, down in slopes:
        product *= count_trees(map, right, down)
    print(product)

if __name__ == "__main__":
    main()