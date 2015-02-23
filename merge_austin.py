"""
>>> A = [1, 3, 5, 7]
>>> B = [2, 4, 6, 8]
>>> merge(A, len(A), B, len(B))
>>> print A
[1, 2, 3, 4, 5, 6, 7, 8]
>>> A = [1, 2, 10]
>>> B = [3, 4, 6, 8, 12, 15, 19, 200]
>>> merge(A, len(A), B, len(B))
>>> print A
[1, 2, 3, 4, 6, 8, 10, 12, 15, 19, 200]
"""


def merge(A, m, B, n):
    """ Merge Sorted Array """

    A.extend([0]*n)
    ptrA = m-1
    ptrB = n-1
    ptrAex = m+n-1

    while True:
        if ptrB < 0:
            #done
            return
        if ptrA < 0:
            # flush remaining B list to A
            A[ptrAex] = B[ptrB]
            ptrAex -= 1
            ptrB -= 1
        else:
            # checking for swaps
            if A[ptrA] > B[ptrB]:
                A[ptrAex] = A[ptrA]
                ptrAex -= 1
                ptrA -= 1
            else:
                A[ptrAex] = B[ptrB]
                ptrAex -= 1
                ptrB -= 1


if __name__ == "__main__":
    import doctest
    doctest.testmod()