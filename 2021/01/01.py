'''
Un essai pour la partie 1
Cinq essais pour la partie 2
'''
def solve_part1(data):
    return sum(b > a for a, b in zip(data, data[1:]))

def solve_part2(data):
    window_sums = [sum(data[i:i+3]) for i in range(len(data)-2)]
    return sum(b > a for a, b in zip(window_sums, window_sums[1:]))

def main():
    with open('01.txt', 'r') as file:
        data = list(map(int, file.read().split()))
    print(f"Part 1: {solve_part1(data)}")
    print(f"Part 2: {solve_part2(data)}")

if __name__ == "__main__":
    main()