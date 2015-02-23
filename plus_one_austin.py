"""
>>> plus_one([0])
[1]
>>> plus_one([9, 9, 9])
[1, 0, 0, 0]
"""


def plus_one(digits):
    """ Plus One """

    overflow = True
    idx = 0
    while overflow:
        idx -= 1
        if -idx > len(digits):
            digits = [1] + digits
            overflow = False
        else:
            digits[idx] += 1
            if digits[idx] > 9:
                digits[idx] = 0
            else:
                overflow = False

    return digits


if __name__ == "__main__":
    import doctest
    doctest.testmod()