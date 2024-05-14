'''
Un essai pour résoudre le jour 6 de l'année 2020.
'''
def main():
    with open('06.txt', 'r') as file:
        groups = file.read().split('\n\n')

    total_any_yes = sum(len(set(group.replace('\n', ''))) for group in groups)
    print(total_any_yes)

    total_all_yes = sum(len(set.intersection(*map(set, group.split('\n')))) for group in groups)
    print(total_all_yes)

if __name__ == "__main__":
    main()