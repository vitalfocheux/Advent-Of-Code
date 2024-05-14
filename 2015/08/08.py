'''
Un essai pour résoudre le jour 8 de l'année 2015
'''
def read_strings(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file]

strings = read_strings('08.txt')

# Part 1
code_chars = sum(len(s) for s in strings)
memory_chars = sum(len(eval(s)) for s in strings)
print(code_chars - memory_chars)

# Part 2
encoded_chars = sum(len(s.replace('\\', '\\\\').replace('"', '\\"')) + 2 for s in strings)
print(encoded_chars - code_chars)