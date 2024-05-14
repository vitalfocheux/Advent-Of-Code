'''
Un essai pour résoudre le jour 1 de l'année 2020.
'''
def find_two_entries_summing_to_2020(entries):
    entries_set = set(entries)
    for entry in entries:
        complement = 2020 - entry
        if complement in entries_set:
            return entry * complement
    return None

def find_three_entries_summing_to_2020(entries):
    entries_set = set(entries)
    for i in range(len(entries)):
        for j in range(i + 1, len(entries)):
            complement = 2020 - entries[i] - entries[j]
            if complement in entries_set:
                return entries[i] * entries[j] * complement
    return None

def main():
    with open('01.txt', 'r') as file:
        entries = [int(line.strip()) for line in file]
    print(find_two_entries_summing_to_2020(entries))
    print(find_three_entries_summing_to_2020(entries))

if __name__ == "__main__":
    main()