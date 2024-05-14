'''
Cinq essais pour résoudre le jour 18 de l'année 2020.
'''
import re

def evaluate_expression(expression):
    # Gérer les parenthèses en premier
    while '(' in expression:
        expression = re.sub(r'\(([^()]+)\)', lambda m: str(evaluate_expression(m.group(1))), expression)
    
    # Évaluer les opérations de gauche à droite
    parts = expression.split()
    while len(parts) > 1:
        a, op, b = parts[:3]
        if op == '+':
            res = int(a) + int(b)
        else:  # op == '*'
            res = int(a) * int(b)
        parts = [str(res)] + parts[3:]
    
    return int(parts[0])

def evaluate_expression_advanced(expression):
    # Gérer les parenthèses en premier
    while '(' in expression:
        expression = re.sub(r'\(([^()]+)\)', lambda m: str(evaluate_expression_advanced(m.group(1))), expression)
    
    # Évaluer les additions
    while '+' in expression:
        expression = re.sub(r'(\d+) \+ (\d+)', lambda m: str(int(m.group(1)) + int(m.group(2))), expression)
    
    # Évaluer les multiplications
    while '*' in expression:
        expression = re.sub(r'(\d+) \* (\d+)', lambda m: str(int(m.group(1)) * int(m.group(2))), expression)
    
    return int(expression)

def main():
    with open('18.txt', 'r') as file:
        expressions = [line.strip() for line in file]

    print(sum(evaluate_expression(expression) for expression in expressions))
    print(sum(evaluate_expression_advanced(expression) for expression in expressions))

if __name__ == "__main__":
    main()