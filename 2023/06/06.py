'''
Un essai pour résoudre le jour 6 de l'année 2023
'''
def calculate_ways_to_win(filename):
    with open(filename, 'r') as file:
        times = list(map(int, file.readline().split()))
        records = list(map(int, file.readline().split()))

    total_ways = 1
    for time, record in zip(times, records):
        ways = 0
        for t in range(1, time):
            if t * (time - t) > record:
                ways += 1
        total_ways *= ways

    return total_ways

print(calculate_ways_to_win('06.txt'))

def calculate_ways_to_win(filename):
    with open(filename, 'r') as file:
        time = int(file.readline().replace(" ", ""))
        record = int(file.readline().replace(" ", ""))

    ways = 0
    for t in range(1, time):
        if t * (time - t) > record:
            ways += 1

    return ways

print(calculate_ways_to_win('06.txt'))