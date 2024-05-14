def solve():
    with open('03.txt') as f:
        rucksacks = [line.strip() for line in f]

    total_priority = 0
    for rucksack in rucksacks:
        mid = len(rucksack) // 2
        compartment1, compartment2 = set(rucksack[:mid]), set(rucksack[mid:])
        common_item = (compartment1 & compartment2).pop()

        if 'a' <= common_item <= 'z':
            priority = ord(common_item) - ord('a') + 1
        else:
            priority = ord(common_item) - ord('A') + 27

        total_priority += priority

    return total_priority

print(solve())

def solve():
    with open('03.txt') as f:
        rucksacks = [line.strip() for line in f]

    total_priority = 0
    for i in range(0, len(rucksacks), 3):
        rucksack1, rucksack2, rucksack3 = set(rucksacks[i]), set(rucksacks[i+1]), set(rucksacks[i+2])
        common_item = (rucksack1 & rucksack2 & rucksack3).pop()

        if 'a' <= common_item <= 'z':
            priority = ord(common_item) - ord('a') + 1
        else:
            priority = ord(common_item) - ord('A') + 27

        total_priority += priority

    return total_priority

print(solve())