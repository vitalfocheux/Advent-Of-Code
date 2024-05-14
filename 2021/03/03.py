'''
Un essai pour la partie 1
La partie 2 ne fonctionne pas
'''
def solve(data):
    gamma_rate = ''
    epsilon_rate = ''
    for i in range(len(data[0])):
        count_1 = sum(line[i] == '1' for line in data)
        count_0 = len(data) - count_1
        gamma_rate += '1' if count_1 > count_0 else '0'
        epsilon_rate += '0' if count_1 > count_0 else '1'
    power_consumption = int(gamma_rate, 2) * int(epsilon_rate, 2)
    return power_consumption

def main():
    with open('03.txt', 'r') as file:
        data = file.read().splitlines()
    print(f"Power consumption: {solve(data)}")

if __name__ == "__main__":
    main()