def create_balanced_parentheses(n):
    balanced_parentheses(n, n, '')

def balanced_parentheses(left_p, right_p, word):
    if left_p == 0 and right_p == 0:
        print(word)

    if left_p > 0:
        balanced_parentheses(left_p - 1, right_p, word + '(')

    if right_p > left_p:
        balanced_parentheses(left_p, right_p - 1, word + ')')

create_balanced_parentheses(3)
