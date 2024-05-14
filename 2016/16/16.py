'''
Un essai pour résoudre le jour 16 de l'Avent de Code 2016
'''
def generate_data(initial, length):
    data = initial
    while len(data) < length:
        b = data[::-1].replace('0', 'x').replace('1', '0').replace('x', '1')
        data = data + '0' + b
    return data[:length]

def calculate_checksum(data):
    checksum = ''
    for i in range(0, len(data), 2):
        if data[i] == data[i+1]:
            checksum += '1'
        else:
            checksum += '0'
    if len(checksum) % 2 == 0:
        return calculate_checksum(checksum)
    else:
        return checksum

# Part 1
data = generate_data('10010000000110000', 272)
print(calculate_checksum(data))

# Part 2
data = generate_data('10010000000110000', 35651584)
print(calculate_checksum(data))