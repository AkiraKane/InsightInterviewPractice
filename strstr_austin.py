"""
>>> str_str(",nkzkergqkwe,kawef", "ker")
4
"""


def str_str(haystack, needle):
    if not needle:
        return 0
    elif not haystack:
        return -1

    for i in range(len(haystack)-len(needle)+1):
        if haystack[i] == needle[0]:
            valid = True
            for j in range(len(needle)):
                if haystack[i+j] != needle[j]:
                    valid = False
                    break
            if valid:
                return i

    return -1