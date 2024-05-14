'''
Un essai pour la partie 1
Deux essais pour la partie 2
'''
def count_differences(adapters):
    differences = [b - a for a, b in zip(adapters, adapters[1:])]
    return differences.count(1) * (differences.count(3) + 1)

def count_arrangements(adapters):
    ways = [0] * (adapters[-1] + 1)
    ways[0] = 1
    for i in range(1, adapters[-1] + 1):
        ways[i] = sum(ways[i - j] for j in range(1, 4) if i - j in adapters)
    return ways[-1]

def main():
    with open('10.txt', 'r') as file:
        adapters = sorted(int(line.strip()) for line in file)
        adapters = [0] + adapters

    print(count_differences(adapters))
    print(count_arrangements(adapters))

if __name__ == "__main__":
    main()