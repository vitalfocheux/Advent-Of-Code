def solve():
    with open('04.txt') as f:
        pairs = [line.strip() for line in f]

    count = 0
    for pair in pairs:
        range1, range2 = pair.split(',')
        start1, end1 = map(int, range1.split('-'))
        start2, end2 = map(int, range2.split('-'))

        if start1 <= start2 <= end2 <= end1 or start2 <= start1 <= end1 <= end2:
            count += 1

    return count

print(solve())

def solve():
    with open('04.txt') as f:
        pairs = [line.strip() for line in f]

    count = 0
    for pair in pairs:
        range1, range2 = pair.split(',')
        start1, end1 = map(int, range1.split('-'))
        start2, end2 = map(int, range2.split('-'))

        if start1 <= end2 and start2 <= end1:
            count += 1

    return count

print(solve())