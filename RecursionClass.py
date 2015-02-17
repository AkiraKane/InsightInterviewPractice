__author__ = 'aouyang1'

import time
import numpy as np
import random

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


maxX = 12
maxY = 12
path_dict = {}
def find_paths_memo(x, y):

    if (x, y) in path_dict:
        return path_dict[(x, y)]

    if x == maxX-1 and y == maxY-1:
        return 1
    else:
        if x+1 > maxX-1:
            path_dict[(x, y+1)] = find_paths_memo(x, y+1)
            return path_dict[(x, y+1)]

        elif y+1 > maxY-1:
            path_dict[(x+1, y)] = find_paths_memo(x+1, y)
            return path_dict[(x+1, y)]

        else:
            down_count = find_paths_memo(x+1, y)
            right_count = find_paths_memo(x, y+1)

            path_dict[(x+1, y)] = down_count
            path_dict[(x, y+1)] = right_count

            return down_count + right_count


def find_paths(x, y):
    if x == maxX-1 and y == maxY-1:
        return 1
    else:
        if x+1 > maxX-1:
            return find_paths(x, y+1)

        elif y+1 > maxY-1:
            return find_paths(x+1, y)

        else:
            return find_paths(x+1, y) + find_paths(x, y+1)


def find_paths_closed_form():
    return 2**((maxX-2)*(maxY-2))+2


def find_magic_dumb(my_list):
    for idx, val in enumerate(my_list):
        if idx == val:
            return idx

    return False


def find_magic(my_list, start_idx, end_idx):
    sub_list = my_list[start_idx:end_idx]
    list_len = len(sub_list)
    curr_idx = list_len/2
    curr_val = sub_list[curr_idx]
    if not sub_list:
        return False
    elif curr_val == curr_idx + start_idx:
        return curr_idx + start_idx
    else:
        if list_len == 1:
            return False
        else:
            if curr_val > curr_idx + start_idx:
                return find_magic(my_list,
                                  start_idx,
                                  start_idx + curr_idx)
            else:
                return find_magic(my_list,
                                  start_idx + curr_idx,
                                  start_idx + list_len)


def permute_string(my_str, curr_perm, perm_list=[]):
    if not my_str:
        return
    else:
        for char_idx in xrange(len(my_str)):
            new_perm = curr_perm + my_str[char_idx]
            sub_str = my_str[:char_idx] + my_str[char_idx+1:len(my_str)]

            perm_list.append(new_perm)

            permute_string(sub_str, new_perm, perm_list)

    return perm_list


def subset_string(my_str):
    subset_list = []
    for num_char_in_sub in xrange(len(my_str)):
        for idx in xrange(len(my_str)-num_char_in_sub):
            subset_list.append(my_str[idx:idx + num_char_in_sub + 1])

    return subset_list








