import hashlib

def md5(data, encoding='utf-8'):
    """Return the md5 hash of the input data"""
    return hashlib.md5(data.encode(encoding)).hexdigest()

def sha256(data, encoding='utf-8'):
    """Return the sha256 hash of the input data"""
    return hashlib.sha256(data.encode(encoding)).hexdigest()

def min_max(data):
    """Return the min and max values of the input data"""
    return min(data), max(data)

def manhattan_distance(p1, p2):
    """Return the Manhattan distance between two points"""
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

def shoelace(tuple):
    """Return the area of a polygon defined by the input points"""
    n = len(tuple)
    return 0.5 * abs(sum(tuple[i][0] * tuple[(i + 1) % n][1] - tuple[(i + 1) % n][0] * tuple[i][1] for i in range(n)))
