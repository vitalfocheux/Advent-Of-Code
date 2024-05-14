'''
Un essai pour résoudre le jour 15 de l'année 2020.
'''
def play_game(starting_numbers, end_turn):
    spoken_numbers = {number: turn for turn, number in enumerate(starting_numbers, start=1)}
    last_number = starting_numbers[-1]
    for turn in range(len(starting_numbers) + 1, end_turn + 1):
        spoken_numbers[last_number], last_number = turn - 1, turn - 1 - spoken_numbers.get(last_number, turn - 1)
    return last_number

def main():
    starting_numbers = [0,12,6,13,20,1,17]  # Replace with your starting numbers

    print(play_game(starting_numbers, end_turn=2020))
    print(play_game(starting_numbers, end_turn=30000000))

if __name__ == "__main__":
    main()