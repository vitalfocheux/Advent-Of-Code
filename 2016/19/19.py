'''
Un essai pour la partie 1
Trois essai pour la partie 2
'''
from collections import deque

def find_last_elf_part1(num_elves):
    elves = list(range(1, num_elves + 1))
    while len(elves) > 1:
        elves = elves[::2] if len(elves) % 2 == 0 else elves[2::2]
    return elves[0]

def find_last_elf_part2(num_elves):
    left = deque(range(1, num_elves // 2 + 1))
    right = deque(range(num_elves // 2 + 1, num_elves + 1))
    while left and right:
        if len(left) > len(right):
            left.pop()
        else:
            right.popleft()
        # Rotate deques
        right.append(left.popleft())
        left.append(right.popleft())
    return left[0] if left else right[0]

num_elves = 3004953

# Part 1
print(find_last_elf_part1(num_elves))

# Part 2
print(find_last_elf_part2(num_elves))