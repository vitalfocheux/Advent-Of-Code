'''
Un essai pour la partie 1
Deux essais pour la partie 2
'''
def calculate_syntax_error_score(navigation_system):
    opening_chars = "([{<"
    closing_chars = ")]}>"
    matching_chars = {")": "(", "]": "[", "}": "{", ">": "<"}
    scores = {")": 3, "]": 57, "}": 1197, ">": 25137}
    total_score = 0

    for line in navigation_system.splitlines():
        stack = []
        for char in line:
            if char in opening_chars:
                stack.append(char)
            elif char in closing_chars:
                if not stack or stack[-1] != matching_chars[char]:
                    total_score += scores[char]
                    break
                stack.pop()

    return total_score

def calculate_completion_scores(navigation_system):
    opening_chars = "([{<"
    closing_chars = ")]}>"
    matching_chars = {")": "(", "]": "[", "}": "{", ">": "<"}
    reverse_matching_chars = {"(": ")", "[": "]", "{": "}", "<": ">"}
    scores = {")": 1, "]": 2, "}": 3, ">": 4}
    completion_scores = []

    for line in navigation_system.splitlines():
        stack = []
        for char in line:
            if char in opening_chars:
                stack.append(char)
            elif char in closing_chars:
                if not stack or stack[-1] != matching_chars[char]:
                    break
                stack.pop()
        else:
            completion_string = "".join(reverse_matching_chars[c] for c in reversed(stack))
            score = 0
            for char in completion_string:
                score = score * 5 + scores[char]
            completion_scores.append(score)

    completion_scores.sort()
    return completion_scores[len(completion_scores) // 2]


input_data = open("10.txt").read()

print(calculate_syntax_error_score(input_data))
print(calculate_completion_scores(input_data)) 