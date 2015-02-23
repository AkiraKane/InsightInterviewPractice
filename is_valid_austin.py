"""
>>> is_valid("{([])([][])}")
True
>>> is_valid("{([])([]])}")
False
"""


def is_valid(s):
    """ Valid Parentheses """

    brackets = {"(": ")", "{": "}", "[": "]"}

    if len(s) % 2 == 1 or s[0] not in brackets:
        return False

    char_stack = []
    for val in s:
        if val in brackets:
            char_stack.append(val)
        elif val == brackets[char_stack[-1]]:
            char_stack.pop()
        else:
            return False

    if len(char_stack) != 0:
        return False

    return True


if __name__ == "__main__":
    import doctest
    doctest.testmod()