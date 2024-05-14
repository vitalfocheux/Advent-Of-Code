'''
Un essai pour résoudre le problème 09 de Advent of Code 2016
'''
def read_input(file_path):
    with open(file_path, 'r') as file:
        return file.read().strip()

def decompress_v1(data):
    decompressed = ''
    i = 0
    while i < len(data):
        if data[i] == '(':
            j = data.index(')', i)
            length, repeat = map(int, data[i+1:j].split('x'))
            decompressed += data[j+1:j+1+length] * repeat
            i = j + 1 + length
        else:
            decompressed += data[i]
            i += 1
    return decompressed

def decompress_v2_length(data):
    length = 0
    i = 0
    while i < len(data):
        if data[i] == '(':
            j = data.index(')', i)
            length_chunk, repeat = map(int, data[i+1:j].split('x'))
            length += repeat * decompress_v2_length(data[j+1:j+1+length_chunk])
            i = j + 1 + length_chunk
        else:
            length += 1
            i += 1
    return length

data = read_input('09.txt')

# Part 1
print(len(decompress_v1(data)))

# Part 2
print(decompress_v2_length(data))