def solve():
    with open('06.txt') as f:
        datastream = f.read().strip()

    buffer = ''
    for i, char in enumerate(datastream, 1):
        buffer += char
        buffer = buffer[-4:]
        if len(set(buffer)) == 4:
            return i

    return -1  # No marker found

print(solve())

def solve():
    with open('06.txt') as f:
        datastream = f.read().strip()

    buffer = ''
    for i, char in enumerate(datastream, 1):
        buffer += char
        buffer = buffer[-14:]
        if len(set(buffer)) == 14:
            return i

    return -1  # No marker found

print(solve())