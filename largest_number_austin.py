"""
>>> compare_str("824", "8247")
1
>>> largest_number([3, 30, 34, 5, 9])
'9534330'
>>> largest_number([0, 0])
'0'
>>> largest_number([824,938,1399,5607,6973,5703,9609,4398,8247])
'9609938824824769735703560743981399'
"""


def compare_str(str1, str2):
    if str1 + str2 > str2 + str1:
        return 1
    elif str1 + str2 < str2 + str1:
        return -1
    else:
        return 0


def merge_str(num1, num2):
    ptr1 = 0
    ptr2 = 0
    new_num = []
    while ptr1 < len(num1) and ptr2 < len(num2):
        if compare_str(num1[ptr1], num2[ptr2]) == 1:
            new_num.append(num1[ptr1])
            ptr1 += 1
        else:
            new_num.append(num2[ptr2])
            ptr2 += 1

    if ptr2 == len(num2):
        new_num.extend(num1[ptr1:])
        return new_num

    if ptr1 == len(num1):
        new_num.extend(num2[ptr2:])
        return new_num


def mergesort_str(num):
    num_len = len(num)
    left = num[:num_len/2]
    right = num[num_len/2:]
    if not right:
        return left
    elif not left:
        return right
    else:
        return merge_str(mergesort_str(left), mergesort_str(right))


def largest_number(num):
    """ Largest Number """

    num = map(lambda x: str(x), num)
    num = mergesort_str(num)
    while num[0] == "0" and len(num) > 1:
        num = num[1:]

    return "".join(num)


if __name__ == "__main__":
    import doctest
    doctest.testmod()



