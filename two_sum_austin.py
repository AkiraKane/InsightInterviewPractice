"""
>>> two_sum([3, 2, 4], 6)
(2, 3)
>>> two_sum([4, 6, 2, 8, 3, 9], 9)
(2, 5)
"""


def two_sum(num, target):
    """ Two Sum """

    num_dict = {}
    for idx, val in enumerate(num):
        num_dict[val] = idx

    for idx, val in enumerate(num):
        search_val = target - val
        if search_val in num_dict:
            if num_dict[search_val] > idx:
                index1 = idx+1
                index2 = num_dict[search_val]+1
                return index1, index2


if __name__ == "__main__":
    import doctest
    doctest.testmod()