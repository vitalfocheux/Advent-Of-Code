'''
Un essai pour résoudre le problème 07 de Advent of Code 2016
'''
import re

def read_ips(file_path):
    with open(file_path, 'r') as file:
        return file.read().splitlines()

def supports_tls(ip):
    bracketed = re.findall(r'\[([a-z]+)\]', ip)
    unbracketed = re.findall(r'([a-z]+)(?=\[|$)', ip)
    return (any(a == d and b == c and a != b for segment in unbracketed for a, b, c, d in zip(segment, segment[1:], segment[2:], segment[3:])) and
            not any(a == d and b == c and a != b for segment in bracketed for a, b, c, d in zip(segment, segment[1:], segment[2:], segment[3:])))

def supports_ssl(ip):
    bracketed = re.findall(r'\[([a-z]+)\]', ip)
    unbracketed = re.findall(r'([a-z]+)(?=\[|$)', ip)
    return any(a == c and a != b and b + a + b in ''.join(bracketed) for segment in unbracketed for a, b, c in zip(segment, segment[1:], segment[2:]))

ips = read_ips('07.txt')

# Part 1
print(sum(supports_tls(ip) for ip in ips))

# Part 2
print(sum(supports_ssl(ip) for ip in ips))