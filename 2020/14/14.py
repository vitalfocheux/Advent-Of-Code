'''
Un essai pour la partie 1
Trois essais pour la partie 2
'''
import re
import itertools

def apply_mask(mask, value):
    value |= int(mask.replace('X', '0'), 2)
    value &= int(mask.replace('X', '1'), 2)
    return value

def apply_mask_v2(mask, address):
    address = list('{:036b}'.format(address))
    for i, bit in enumerate(mask):
        if bit != '0':
            address[i] = bit

    floating = [i for i, bit in enumerate(address) if bit == 'X']
    for combination in itertools.product([0, 1], repeat=len(floating)):
        result = list(address)
        for i, bit in zip(floating, combination):
            result[i] = str(bit)
        yield int(''.join(result), 2)

def execute_program(lines, version):
    memory = {}
    for line in lines:
        if line.startswith('mask'):
            mask = line.split('=')[1].strip()
        else:
            address, value = map(int, re.findall(r'\d+', line))
            if version == 1:
                memory[address] = apply_mask(mask, value)
            else:
                for address in apply_mask_v2(mask, address):
                    memory[address] = value
    return sum(memory.values())

def main():
    with open('14.txt', 'r') as file:
        lines = file.read().splitlines()

    print(execute_program(lines, version=1))
    print(execute_program(lines, version=2))

if __name__ == "__main__":
    main()