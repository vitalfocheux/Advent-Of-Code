'''
Un essai pour résoudre le jour 2 de l'année 2015
'''
def read_boxes(file_path):
    with open(file_path, 'r') as file:
        return [list(map(int, line.split('x'))) for line in file]

def part1(boxes):
    total_paper = 0
    for l, w, h in boxes:
        sides = [l*w, w*h, h*l]
        total_paper += 2 * sum(sides) + min(sides)
    return total_paper

def part2(boxes):
    total_ribbon = 0
    for l, w, h in boxes:
        total_ribbon += 2 * sum(sorted([l, w, h])[:2]) + l * w * h
    return total_ribbon

boxes = read_boxes('02.txt')

# Part 1
print(part1(boxes))

# Part 2
print(part2(boxes))