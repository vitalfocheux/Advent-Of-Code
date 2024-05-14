'''
Un essai pour la partie 1
'''
def parse_input(file):
    with open(file, 'r') as f:
        jobs = {line.split(': ')[0]: line.split(': ')[1].strip() for line in f}
    return jobs

def calculate_number(monkey, jobs, memo):
    if monkey in memo:
        return memo[monkey]
    job = jobs[monkey]
    if job.isdigit() or (job.startswith('-') and job[1:].isdigit()):
        memo[monkey] = int(job)
    else:
        operand1, operation, operand2 = job.split()
        num1 = calculate_number(operand1, jobs, memo)
        num2 = calculate_number(operand2, jobs, memo)
        if operation == '+':
            memo[monkey] = num1 + num2
        elif operation == '-':
            memo[monkey] = num1 - num2
        elif operation == '*':
            memo[monkey] = num1 * num2
        elif operation == '/':
            memo[monkey] = num1 // num2
    return memo[monkey]

def main():
    jobs = parse_input('21.txt')
    memo = {}
    return calculate_number('root', jobs, memo)

print(main())