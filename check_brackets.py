# python3

import sys

class Bracket:
    def __init__(self, bracket_type, position):
        self.bracket_type = bracket_type
        self.position = position

    def Match(self, c):
        if self.bracket_type == '[' and c == ']':
            return True
        if self.bracket_type == '{' and c == '}':
            return True
        if self.bracket_type == '(' and c == ')':
            return True
        return False

if __name__ == "__main__":
    text = sys.stdin.read()

    first_unmatched_closing_bracket_index = None
    opening_brackets_stack = []
    for i, next in enumerate(text):
        if next == '(' or next == '[' or next == '{':
            opening_brackets_stack.append(Bracket(next, i))
            pass

        if next == ')' or next == ']' or next == '}':
            if len(opening_brackets_stack) and opening_brackets_stack[-1].Match(next):
                opening_brackets_stack.pop()
                pass
            else:
                first_unmatched_closing_bracket_index = i
                break

    if first_unmatched_closing_bracket_index != None:
        print(first_unmatched_closing_bracket_index + 1)
    elif len(opening_brackets_stack) > 0:
        print(opening_brackets_stack[0].position + 1)
    else:
        print('Success')
