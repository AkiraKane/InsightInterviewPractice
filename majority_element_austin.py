"""
>>> majority_element([1, 2, 3, 4, 4, 4, 7, 2, 3])
4
"""


def majority_element(num):
    """ Majority Element """

    elem = {}
    maj_elem = num[0]
    for val in num:
        if val not in elem:
            elem[val] = 1
        else:
            elem[val] += 1
            if elem[val] > elem[maj_elem]:
                maj_elem = val

    return maj_elem


if __name__ == "__main__":
    import doctest
    doctest.testmod()