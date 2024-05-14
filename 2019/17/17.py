'''
Trois essais pour la partie 1
La partie 2 ne fonctionne pas
'''
class Intcode:
    def __init__(self, program):
        self.program = program + [0] * 10000
        self.ip = 0
        self.relative_base = 0

    def run(self, inputs):
        inputs = inputs[::-1]
        outputs = []
        while True:
            opcode = self.program[self.ip] % 100
            modes = [self.program[self.ip] // 100 // 10**i % 10 for i in range(3)]
            if opcode == 99:
                return outputs
            elif opcode in [1, 2, 7, 8]:
                a = self.get_value(1, modes[0])
                b = self.get_value(2, modes[1])
                if opcode == 1:
                    self.program[self.get_address(3, modes[2])] = a + b
                elif opcode == 2:
                    self.program[self.get_address(3, modes[2])] = a * b
                elif opcode == 7:
                    self.program[self.get_address(3, modes[2])] = int(a < b)
                elif opcode == 8:
                    self.program[self.get_address(3, modes[2])] = int(a == b)
                self.ip += 4
            elif opcode in [3, 4]:
                if opcode == 3:
                    if not inputs:
                        return outputs
                    self.program[self.get_address(1, modes[0])] = inputs.pop()
                elif opcode == 4:
                    outputs.append(self.get_value(1, modes[0]))
                self.ip += 2
            elif opcode in [5, 6]:
                a = self.get_value(1, modes[0])
                b = self.get_value(2, modes[1])
                if opcode == 5 and a != 0 or opcode == 6 and a == 0:
                    self.ip = b
                else:
                    self.ip += 3
            elif opcode == 9:
                self.relative_base += self.get_value(1, modes[0])
                self.ip += 2

    def get_value(self, offset, mode):
        if mode == 0:
            return self.program[self.program[self.ip + offset]]
        elif mode == 1:
            return self.program[self.ip + offset]
        elif mode == 2:
            return self.program[self.relative_base + self.program[self.ip + offset]]

    def get_address(self, offset, mode):
        if mode == 0:
            return self.program[self.ip + offset]
        elif mode == 2:
            return self.relative_base + self.program[self.ip + offset]

def get_map(program):
    machine = Intcode(program)
    output = machine.run([])
    return ''.join(map(chr, output)).strip()

def get_intersections(map):
    lines = map.split('\n')
    intersections = []
    for y in range(1, len(lines) - 1):
        for x in range(1, len(lines[0]) - 1):
            if lines[y][x] == lines[y-1][x] == lines[y+1][x] == lines[y][x-1] == lines[y][x+1] == '#':
                intersections.append((x, y))
    return intersections

def part1(program):
    map = get_map(program)
    intersections = get_intersections(map)
    return sum(x * y for x, y in intersections)

def part2(program):
    program[0] = 2
    machine = Intcode(program)
    main_routine = 'A,B,C,B,A,C\n'
    function_a = 'R,8,R,8\n'  # Replace with the correct movements for function A
    function_b = 'R,4,R,4,R,8\n'  # Replace with the correct movements for function B
    function_c = 'L,6,L,2\n'  # Replace with the correct movements for function C
    video_feed = 'n\n'
    input = list(map(ord, main_routine + function_a + function_b + function_c + video_feed))
    output = machine.run(input)
    return output[-1]

program = list(map(int, open('17.txt').read().strip().split(',')))
print("Part 1:", part1(program))
print("Part 2:", part2(program))