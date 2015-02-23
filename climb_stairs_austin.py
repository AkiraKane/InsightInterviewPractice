"""
>>> climb_stairs(5)
8
>>> climb_stairs(20)
10946
"""


def climb_stairs(n):
    """ Climbing Stairs """

    arr = []
    for i in range(n+1):
        if i <= 1:
            arr.append(1)
        else:
            arr.append(arr[-1]+arr[-2])
    return arr[-1]


if __name__ == "__main__":
    import doctest
    doctest.testmod()