'''
Un essai pour résoudre le jour 13 de l'année 2020.
'''
def earliest_bus(timestamp, buses):
    wait_times = [(bus - timestamp % bus, bus) for bus in buses if bus]
    wait_time, bus = min(wait_times)
    return wait_time * bus

def earliest_timestamp(buses):
    timestamp, step = 0, 1
    for offset, bus in enumerate(buses):
        if bus:
            while (timestamp + offset) % bus:
                timestamp += step
            step *= bus
    return timestamp

def main():
    with open('13.txt', 'r') as file:
        lines = file.read().splitlines()
        timestamp = int(lines[0])
        buses = [int(bus) if bus != 'x' else None for bus in lines[1].split(',')]

    print(earliest_bus(timestamp, buses))
    print(earliest_timestamp(buses))

if __name__ == "__main__":
    main()