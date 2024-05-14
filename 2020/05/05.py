'''
Un essai pour résoudre le jour 5 de l'année 2020.
'''
def get_seat_id(boarding_pass):
    return int(boarding_pass.replace('F', '0').replace('B', '1').replace('L', '0').replace('R', '1'), 2)

def main():
    with open('05.txt', 'r') as file:
        boarding_passes = [line.strip() for line in file]

    seat_ids = [get_seat_id(boarding_pass) for boarding_pass in boarding_passes]

    print(max(seat_ids))

    all_seat_ids = set(range(min(seat_ids), max(seat_ids) + 1))
    print(all_seat_ids.difference(seat_ids).pop())

if __name__ == "__main__":
    main()