__author__ = 'aouyang1'


def listsum(num_list):
    if not num_list:
        return 0
    elif len(num_list) == 1:
        return num_list[0]
    else:
        return num_list[0] + listsum(num_list[1:])


def tostring(some_num):
    string_arr = "0123456789"
    if some_num < 10:
        return string_arr[some_num % 10]
    else:
        return tostring(some_num/10) + string_arr[some_num % 10]