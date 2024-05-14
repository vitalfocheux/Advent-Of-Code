'''
Un essai pour la partie 1
La partie 2 ne fonctionne pas
'''
from collections import defaultdict
from math import prod

def parse_tiles(input):
    tiles = {}
    for tile in input.strip().split('\n\n'):
        lines = tile.split('\n')
        id = int(lines[0][5:-1])
        tiles[id] = [list(row) for row in lines[1:]]
    return tiles

def get_edges(tile):
    return [''.join(row) for row in [tile[0], tile[-1], [row[0] for row in tile], [row[-1] for row in tile]]]

def get_matching_tiles(tiles):
    edges = defaultdict(list)
    for id, tile in tiles.items():
        for edge in get_edges(tile):
            edges[edge].append(id)
            edges[edge[::-1]].append(id)
    matches = defaultdict(set)
    for edge, ids in edges.items():
        for id in ids:
            matches[id].update(set(ids) - {id})
    return matches

def solve(input):
    tiles = parse_tiles(input)
    matches = get_matching_tiles(tiles)
    corners = [id for id, match in matches.items() if len(match) == 2]
    return prod(corners)

input = open('20.txt').read()

print(solve(input))