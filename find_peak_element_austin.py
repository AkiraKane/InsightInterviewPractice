"""
>>> find_peak_element([3, 2])
0
>>> find_peak_element([1, 2, 3])
2
>>> find_peak_element([0, 1, 2, 3, 2])
3
"""


def slope(val0, val1):
    if val1 > val0:
        return 1
    elif val1 < val0:
        return -1
    else:
        return 0


def find_peak_element(num):
    """ Find Peak Element """

    num_len = len(num)
    if num_len == 1:
        return 0
    elif num_len >= 2:
        if slope(num[0], num[1]) == -1:
            return 0

        if num_len >= 3:
            curr_slope = slope(num[0], num[1])

            for idx in range(num_len-2):
                next_slope = slope(num[idx+1], num[idx+2])
                if curr_slope == 1 and next_slope == -1:
                    return idx + 1

                curr_slope = next_slope

        if slope(num[num_len-2], num[num_len-1]) == 1:
            return num_len - 1
