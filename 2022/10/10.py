'''
Partie 1 réussi du premier coup avec Llama3-70b-8192
La partie 2 ne fonctionne pas
'''
def execute_program(program):
    x = 1
    cycle = 0
    signal_strengths = []
    for instruction in program:
        if instruction.startswith("noop"):
            cycle += 1
            if cycle in [20, 60, 100, 140, 180, 220]:
                signal_strengths.append(cycle * x)
        else:
            _, value = instruction.split()
            value = int(value)
            for _ in range(2):
                cycle += 1
                if cycle in [20, 60, 100, 140, 180, 220]:
                    signal_strengths.append(cycle * x)
            x += value
    return sum(signal_strengths)

with open("10.txt", "r") as f:
    program = [line.strip() for line in f.readlines()]

print(execute_program(program))

