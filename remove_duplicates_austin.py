"""
>>> A = [1, 1, 2, 2, 2, 3, 3, 5, 7]
>>> idx = remove_duplicates(A)
>>> print idx, A[:idx]
5 [1, 2, 3, 5, 7]
"""


def remove_duplicates(A):
    """ Remove Duplicates from Sorted Array """

    if not A:
        return

    a_idx = 0
    for idx, val in enumerate(A):
        if A[a_idx] != val:
            a_idx += 1
            A[a_idx], A[idx] = A[idx], A[a_idx]

    return a_idx+1


if __name__ == "__main__":
    import doctest
    doctest.testmod()