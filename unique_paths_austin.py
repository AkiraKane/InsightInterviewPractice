"""
>>> unique_paths(2, 2)
2
>>> unique_paths(3, 3)
6
>>> unique_paths(10, 10)
48620
>>> unique_paths(12, 12)
705432
>>> unique_paths(100, 100)
22750883079422934966181954039568885395604168260154104734000L
"""

memo = {}


def unique_paths(m, n):
    """ Unique Paths """

    if m == 1 and n == 1:
        return 1

    if m == 1:
        if (m, n-1) not in memo:
            memo[(m, n-1)] = unique_paths(m, n-1)
        return memo[(m, n-1)]

    elif n == 1:
        if (m-1, n) not in memo:
            memo[(m-1, n)] = unique_paths(m-1, n)
        return memo[(m-1, n)]
    else:
        if (m, n-1) not in memo:
            memo[(m, n-1)] = unique_paths(m, n-1)

        if (m-1, n) not in memo:
            memo[(m-1, n)] = unique_paths(m-1, n)

        return memo[(m, n-1)] + memo[(m-1, n)]