'''
Un essai pour résoudre le jour 15 du calendrier de l'avent 2023.
'''
def hash_algorithm(step):
    current_value = 0
    for char in step:
        ascii_code = ord(char)
        current_value += ascii_code
        current_value *= 17
        current_value %= 256
    return current_value

def sum_of_hash_results(filename):
    with open(filename, 'r') as file:
        data = file.read().replace('\n', '')
    steps = data.split(',')
    return sum(hash_algorithm(step) for step in steps)

print(sum_of_hash_results('15.txt'))

def hashmap(filename):
    boxes = [[] for _ in range(256)]

    with open(filename, 'r') as file:
        data = file.read().replace('\n', '')
    steps = data.split(',')

    for step in steps:
        label, operation = step.split('=') if '=' in step else step.split('-')
        box_number = hash_algorithm(label)

        if operation == '':
            boxes[box_number] = [lens for lens in boxes[box_number] if lens[0] != label]
        else:
            focal_length = int(operation)
            for i, lens in enumerate(boxes[box_number]):
                if lens[0] == label:
                    boxes[box_number][i] = (label, focal_length)
                    break
            else:
                boxes[box_number].append((label, focal_length))

    focusing_power = 0
    for box_number, box in enumerate(boxes):
        for slot_number, lens in enumerate(box, start=1):
            focusing_power += (box_number + 1) * slot_number * lens[1]

    return focusing_power

print(hashmap('15.txt'))