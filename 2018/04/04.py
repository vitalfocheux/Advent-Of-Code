'''
Un essaie pour résoudre le jour 4 de l'année 2018
'''
import re
from collections import defaultdict
from datetime import datetime

def parse_records(records):
    records.sort()
    sleep_schedule = defaultdict(list)
    for record in records:
        time, action = record.split('] ')
        time = datetime.strptime(time, '[%Y-%m-%d %H:%M')
        if 'begins shift' in action:
            guard = int(re.search(r'\d+', action).group())
        elif 'falls asleep' in action:
            start = time
        elif 'wakes up' in action:
            sleep_schedule[guard].append((start.minute, time.minute))
    return sleep_schedule

def solve_part1(sleep_schedule):
    guard, periods = max(sleep_schedule.items(), key=lambda item: sum(end - start for start, end in item[1]))
    minutes = [0] * 60
    for start, end in periods:
        for minute in range(start, end):
            minutes[minute] += 1
    minute = minutes.index(max(minutes))
    return guard * minute

def solve_part2(sleep_schedule):
    guard = minute = max_minutes = 0
    for g, periods in sleep_schedule.items():
        minutes = [0] * 60
        for start, end in periods:
            for m in range(start, end):
                minutes[m] += 1
        if max(minutes) > max_minutes:
            guard, minute, max_minutes = g, minutes.index(max(minutes)), max(minutes)
    return guard * minute

# Assuming records is a list of strings read from the input file
with open('04.txt', 'r') as file:
    records = [line.strip() for line in file]

sleep_schedule = parse_records(records)
print(solve_part1(sleep_schedule))  # Part 1
print(solve_part2(sleep_schedule))  # Part 2