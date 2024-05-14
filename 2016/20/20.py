'''
Un essai pour résoudre le jour 20 de l'Avent de Code 2016
'''
def read_input(file_path):
    with open(file_path) as f:
        return [list(map(int, line.strip().split('-'))) for line in f]

def find_lowest_unblocked_ip(ranges):
    ranges.sort()
    lowest_unblocked = 0
    for start, end in ranges:
        if start <= lowest_unblocked <= end:
            lowest_unblocked = end + 1
    return lowest_unblocked

def find_total_unblocked_ips(ranges):
    ranges.sort()
    total_unblocked = 0
    highest_blocked = -1
    for start, end in ranges:
        if start > highest_blocked + 1:
            total_unblocked += start - highest_blocked - 1
        highest_blocked = max(highest_blocked, end)
    return total_unblocked + 2**32 - highest_blocked - 1

ranges = read_input('20.txt')

# Part 1
print(find_lowest_unblocked_ip(ranges))

# Part 2
print(find_total_unblocked_ips(ranges))