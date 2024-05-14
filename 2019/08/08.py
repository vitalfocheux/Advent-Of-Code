'''
Un essai pour résoudre le jour 8 de l'année 2019 du site Advent of Code
'''
def part1(data, width, height):
    layers = [data[i:i+width*height] for i in range(0, len(data), width*height)]
    min_zeros_layer = min(layers, key=lambda layer: layer.count('0'))
    return min_zeros_layer.count('1') * min_zeros_layer.count('2')

def part2(data, width, height):
    layers = [data[i:i+width*height] for i in range(0, len(data), width*height)]
    image = ['2'] * (width * height)
    for layer in layers:
        for i, pixel in enumerate(layer):
            if image[i] == '2':
                image[i] = pixel
    rows = [image[i:i+width] for i in range(0, len(image), width)]
    for row in rows:
        print(''.join(' ' if pixel == '0' else '#' for pixel in row))

data = open('08.txt').read().strip()
width, height = 25, 6

print(part1(data, width, height))  # Part 1
part2(data, width, height)  # Part 2