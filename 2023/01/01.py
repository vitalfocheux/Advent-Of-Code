'''
Un essai pour la partie 1 avec Llama3-70b-8192
La partie 2 ne fonctionne pas
'''
with open('01.txt', 'r') as f:
    lines = f.readlines()

calibration_values = []
for line in lines:
    first_digit = None
    last_digit = None
    for char in line.strip():
        if char.isdigit():
            if first_digit is None:
                first_digit = char
            last_digit = char
    calibration_value = int(first_digit + last_digit)
    calibration_values.append(calibration_value)

print(sum(calibration_values))