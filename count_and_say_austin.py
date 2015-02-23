"""
>>> count_and_say(5)
'111221'
>>> count_and_say(6)
'312211'
>>> count_and_say(10)
'13211311123113112211'
"""


def count_and_say(n):
    """ Count and Say """

    num_list = [1]
    for i in range(n-1):
        curr_val = num_list[0]
        val_cnt = 0
        list_str = []
        for val in num_list:
            if val == curr_val:
                val_cnt += 1
            else:
                list_str.append(val_cnt)
                list_str.append(curr_val)
                curr_val = val
                val_cnt = 1
        list_str.append(val_cnt)
        list_str.append(curr_val)

        num_list = list_str

    return reduce(lambda x, y: x+y, map(lambda x: str(x), num_list))


if __name__ == "__main__":
    import doctest
    doctest.testmod()