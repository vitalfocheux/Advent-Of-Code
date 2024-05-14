'''
Un essai pour résoudre le jour 9 de l'année 2020.
'''
def find_invalid(numbers, preamble):
    for i in range(preamble, len(numbers)):
        if not any(numbers[i] - numbers[j] in numbers[i-preamble:i] for j in range(i-preamble, i)):
            return numbers[i]

def find_contiguous_set(numbers, invalid_number):
    for i in range(len(numbers)):
        for j in range(i+2, len(numbers)):
            if sum(numbers[i:j]) == invalid_number:
                return min(numbers[i:j]) + max(numbers[i:j])

def main():
    with open('09.txt', 'r') as file:
        numbers = [int(line.strip()) for line in file]

    invalid_number = find_invalid(numbers, 25)
    print(invalid_number)
    print(find_contiguous_set(numbers, invalid_number))

if __name__ == "__main__":
    main()