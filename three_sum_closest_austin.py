"""
>>> three_sum_closest([0, 1, 2, -3], 1)
0
>>> three_sum_closest([5, 7, -4, -10, 0, 12, 21, -3], 15)
15
"""


def three_sum_closest(num, target):
    """ 3Sum Closest """

    num.sort()
    curr_sum = None
    curr_delta = None
    jk_sum = {}
    for i in range(len(num)-2):
        j = i+1
        k = len(num)-1
        while j != k:
            if (j, k) not in jk_sum:
                jk_sum[(j, k)] = num[j] + num[k]

            temp_sum = num[i] + jk_sum[(j, k)]
            if temp_sum == target:
                return target
            elif temp_sum < target:
                j += 1
            else:
                k -= 1

            temp_delta = temp_sum - target
            if temp_delta < 0:
                temp_delta *= -1

            if curr_sum is None or temp_delta < curr_delta:
                curr_sum = temp_sum
                curr_delta = temp_delta

    return curr_sum


if __name__ == "__main__":
    import doctest
    doctest.testmod()
