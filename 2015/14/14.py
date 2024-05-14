'''
Un essai pour résoudre le jour 14 de l'année 2015
'''
def read_reindeers(file_path):
    reindeers = {}
    with open(file_path, 'r') as file:
        for line in file:
            name, _, _, speed, _, _, fly_time, _, _, _, _, _, _, rest_time, _ = line.split()
            reindeers[name] = (int(speed), int(fly_time), int(rest_time))
    return reindeers

def simulate_race(reindeers, race_time):
    distances = {name: 0 for name in reindeers}
    for _ in range(race_time):
        for name, (speed, fly_time, rest_time) in reindeers.items():
            if _ % (fly_time + rest_time) < fly_time:
                distances[name] += speed
    return distances

def simulate_race_with_points(reindeers, race_time):
    distances = {name: 0 for name in reindeers}
    points = {name: 0 for name in reindeers}
    for _ in range(race_time):
        for name, (speed, fly_time, rest_time) in reindeers.items():
            if _ % (fly_time + rest_time) < fly_time:
                distances[name] += speed
        leading_distance = max(distances.values())
        for name in reindeers:
            if distances[name] == leading_distance:
                points[name] += 1
    return points

reindeers = read_reindeers('14.txt')

# Part 1
distances = simulate_race(reindeers, 2503)
print(max(distances.values()))

# Part 2
points = simulate_race_with_points(reindeers, 2503)
print(max(points.values()))