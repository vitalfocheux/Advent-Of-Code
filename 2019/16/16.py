def fft_phase(input):
    output = []
    for i in range(len(input)):
        pattern = [0]*(i+1) + [1]*(i+1) + [0]*(i+1) + [-1]*(i+1)
        pattern = pattern * ((len(input)//len(pattern)) + 1)
        pattern = pattern[1:len(input)+1]
        total = sum(a * b for a, b in zip(input, pattern))
        output.append(abs(total) % 10)
    return output

def part1(input):
    for _ in range(100):
        input = fft_phase(input)
    return ''.join(map(str, input[:8]))

def part2(input):
    offset = int(''.join(map(str, input[:7])))
    input = (input * 10000)[offset:]
    for _ in range(100):
        for i in range(len(input)-2, -1, -1):
            input[i] = (input[i] + input[i+1]) % 10
    return ''.join(map(str, input[:8]))

input = list(map(int, open('16.txt').read().strip()))
print("Part 1:", part1(input))
print("Part 2:", part2(input))