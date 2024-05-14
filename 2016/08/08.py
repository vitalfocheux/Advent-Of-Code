'''
Un essai pour résoudre le problème 08 de Advent of Code 2016
'''
import re

def read_instructions(file_path):
    with open(file_path, 'r') as file:
        return file.read().splitlines()

def execute_instructions(instructions, width, height):
    screen = [[0]*width for _ in range(height)]
    for instruction in instructions:
        if match := re.match(r'rect (\d+)x(\d+)', instruction):
            w, h = map(int, match.groups())
            for x in range(w):
                for y in range(h):
                    screen[y][x] = 1
        elif match := re.match(r'rotate row y=(\d+) by (\d+)', instruction):
            y, by = map(int, match.groups())
            screen[y] = screen[y][-by:] + screen[y][:-by]
        elif match := re.match(r'rotate column x=(\d+) by (\d+)', instruction):
            x, by = map(int, match.groups())
            column = [row[x] for row in screen]
            column = column[-by:] + column[:-by]
            for y, value in enumerate(column):
                screen[y][x] = value
    return screen

def count_lit_pixels(screen):
    return sum(sum(row) for row in screen)

def print_screen(screen):
    for row in screen:
        print(''.join('#' if pixel else ' ' for pixel in row))

instructions = read_instructions('08.txt')
screen = execute_instructions(instructions, 50, 6)

# Part 1
print(count_lit_pixels(screen))

# Part 2
print_screen(screen)