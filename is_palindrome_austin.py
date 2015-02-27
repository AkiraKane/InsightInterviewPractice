"""
>>> is_palindrome("aA")
True
>>> is_palindrome("1aA2")
False
>>> is_palindrome("ra c,e.c:ar")
True
"""


def is_palindrome(s):
    """ Is Valid Palindrome """

    if s is None:
        return True

    m = 0
    n = len(s)-1
    while m < n:
        while not s[m].isalnum():
            m += 1
            if m > n:
                return True

        while not s[n].isalnum():
            n -= 1
            if m > n:
                return True

        if s[m].lower() != s[n].lower():
            return False

        m += 1
        n -= 1

    return True

