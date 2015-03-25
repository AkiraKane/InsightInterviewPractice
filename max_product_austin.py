"""
>>> A = [2, 3, -2, 4]
>>> max_product(A)
6
>>> A = [-7, -4, -2, 4]
>>> max_product(A)
28
>>> A = [2, 3]
>>> max_product(A)
6
>>> A = [2, 3, 9, 4]
>>> max_product(A)
36
>>> A = [-2, -3, -2, 0]
>>> max_product(A)
6
>>> A = [-2, -10, 2, 3, -2, 4, 20]
>>> max_product(A)
80
>>> A = [0, 0, 0, 0]
>>> max_product(A)
0
"""


def max_product(A):
    if not A:
        return

    if len(A) == 1:
        return A[0]
    else:
        max_prod = None
        for ind in range(len(A)-1):
            if A[ind] <= 0:
                if A[ind+1] >= 0:
                    curr_prod = A[ind+1]
                else:
                    curr_prod = A[ind] * A[ind+1]
            else:
                curr_prod = A[ind] * A[ind+1]

            if curr_prod > max_prod:
                max_prod = curr_prod

        return max_prod

