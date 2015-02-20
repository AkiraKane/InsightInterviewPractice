def testIsValid():
    assert isValid("(([]))") is True
    assert isValid("([]}") is False


def isValid(s):
    """
    for each char inside for loop,
        if char is an opening parenthesis:
            we push it onto our stack
        else
            we check if it is the correct closing parenthesis for
            last item in stack
            (return False if not correct)
            if correct we pop the last item in stack
    if either stack or remaining list is not empty return False
    return True
    """
    parentheses = {'(': ')', '{': '}', '[': ']'}
    s_list = list(s)
    stack = []
    for char_position in range(len(s_list)):
        char = s_list.pop(0)
        if char in parentheses:
            stack.append(char)
        else:
            if char != parentheses[stack[-1]]:
                return False
            stack.pop()
    if len(stack) + len(s_list) > 0:
        return False
    return True


testIsValid()
