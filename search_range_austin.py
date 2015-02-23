"""
>>> search_range([1, 2, 4, 5, 7, 7, 7, 8, 8, 8], 8)
[7, 9]
>>> search_range([1, 2, 4, 5, 7, 7, 7, 8, 8, 8], 3)
[-1, -1]
"""


def midpoint(start, end):
    return (end-start)/2 + start


def search_range(A, target):
    """ Search for a Range """

    # find a single target
    ptr_l, ptr_r = -1, -1
    imin, imax = 0, len(A)-1
    while imax >= imin:

        ptr = midpoint(imin, imax)
        if A[ptr] == target:
            ptr_l = ptr
            ptr_r = ptr
            break
        elif A[ptr] > target:
            imax = ptr-1
        else:
            imin = ptr+1

    # search for neighboring targets if present
    if ptr_l != -1 and ptr_r != -1:
        at_beg = ptr_l == 0
        while not at_beg:
            if A[ptr_l-1] == target:
                ptr_l -= 1
            else:
                break
            at_beg = ptr_l == 0

        at_end = ptr_r == len(A)-1
        while not at_end:
            if A[ptr_r+1] == target:
                ptr_r += 1
            else:
                break
            at_end = ptr_r == len(A)-1

    return [ptr_l, ptr_r]


if __name__ == "__main__":
    import doctest
    doctest.testmod()