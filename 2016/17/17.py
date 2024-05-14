'''
Deux essais pour résoudre le jour 17 de l'Avent de Code 2016
'''
import hashlib
from collections import deque

def is_open(c):
    return c in 'bcdef'

def get_moves(path, x, y):
    h = hashlib.md5(('hhhxzeay' + path).encode('utf-8')).hexdigest()[:4]
    moves = []
    if is_open(h[0]) and y > 0:
        moves.append((x, y - 1, path + 'U'))
    if is_open(h[1]) and y < 3:
        moves.append((x, y + 1, path + 'D'))
    if is_open(h[2]) and x > 0:
        moves.append((x - 1, y, path + 'L'))
    if is_open(h[3]) and x < 3:
        moves.append((x + 1, y, path + 'R'))
    return moves

def bfs():
    queue = deque([(0, 0, '')])
    last_path = None
    while queue:
        x, y, path = queue.popleft()
        if (x, y) == (3, 3):
            if not last_path:
                print('Part 1:', path)
            last_path = path
        else:
            for move in get_moves(path, x, y):
                queue.append(move)
    return last_path

# Part 1 and Part 2
last_path = bfs()
if last_path is not None:
    print('Part 2:', len(last_path))
else:
    print('No path found')