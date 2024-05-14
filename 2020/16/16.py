'''
Un essai pour résoudre le jour 16 de l'année 2020.
'''
import re

def parse_input(input):
    rules, my_ticket, nearby_tickets = input.split('\n\n')
    rules = {field: [(int(a), int(b)) for a, b in re.findall(r'(\d+)-(\d+)', ranges)] for field, ranges in re.findall(r'(.+): (.+)', rules)}
    my_ticket = list(map(int, my_ticket.splitlines()[1].split(',')))
    nearby_tickets = [list(map(int, line.split(','))) for line in nearby_tickets.splitlines()[1:]]
    return rules, my_ticket, nearby_tickets

def validate_tickets(rules, tickets):
    valid_tickets = []
    error_rate = 0
    for ticket in tickets:
        valid = True
        for value in ticket:
            if not any(a <= value <= b for ranges in rules.values() for a, b in ranges):
                error_rate += value
                valid = False
        if valid:
            valid_tickets.append(ticket)
    return error_rate, valid_tickets

def identify_fields(rules, valid_tickets):
    possible_fields = {i: set(rules.keys()) for i in range(len(valid_tickets[0]))}
    for ticket in valid_tickets:
        for i, value in enumerate(ticket):
            possible_fields[i] &= {field for field, ranges in rules.items() if any(a <= value <= b for a, b in ranges)}
    identified_fields = {}
    while possible_fields:
        i, field = next((i, fields.pop()) for i, fields in possible_fields.items() if len(fields) == 1)
        identified_fields[field] = i
        del possible_fields[i]
        for fields in possible_fields.values():
            fields.discard(field)
    return identified_fields

def main():
    with open('16.txt', 'r') as file:
        rules, my_ticket, nearby_tickets = parse_input(file.read())

    error_rate, valid_tickets = validate_tickets(rules, nearby_tickets)
    print(error_rate)

    identified_fields = identify_fields(rules, valid_tickets)
    departure_values = [my_ticket[i] for field, i in identified_fields.items() if field.startswith('departure')]
    product = 1
    print([product := product * value for value in departure_values][-1])

if __name__ == "__main__":
    main()