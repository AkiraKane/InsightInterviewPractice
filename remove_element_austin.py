"""
>>> remove_element([4,5,4], 4)
1
>>> remove_element([1], 1)
0
>>> remove_element([1, 4, 3, 1, 7, 2, 8, 2, 9, 3, 10, 3, 3, 3, 5], 3)
10
"""


def remove_element(a, elem):
    """ Remove Element """

    if not a:
        return

    a_len = len(a)
    a_idx = a_len-1
    for idx in range(a_len):
        if a[a_len-idx-1] == elem:
            a[a_len-idx-1], a[a_idx] = a[a_idx], a[a_len-idx-1]
            a_idx -= 1

    return a_idx+1


if __name__ == "__main__":
    import doctest
    doctest.testmod()

