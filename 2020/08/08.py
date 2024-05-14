'''
Un essai pour résoudre le jour 8 de l'année 2020.
'''
def execute(instructions):
    acc = 0
    pc = 0
    executed = set()

    while pc not in executed and pc < len(instructions):
        executed.add(pc)
        op, arg = instructions[pc]
        if op == 'acc':
            acc += arg
            pc += 1
        elif op == 'jmp':
            pc += arg
        elif op == 'nop':
            pc += 1

    return acc, pc == len(instructions)

def main():
    with open('08.txt', 'r') as file:
        instructions = [(line.split()[0], int(line.split()[1])) for line in file]

    print(execute(instructions)[0])

    for i, (op, arg) in enumerate(instructions):
        if op in ('jmp', 'nop'):
            instructions[i] = ('nop' if op == 'jmp' else 'jmp', arg)
            acc, terminated = execute(instructions)
            if terminated:
                print(acc)
                break
            instructions[i] = (op, arg)

if __name__ == "__main__":
    main()