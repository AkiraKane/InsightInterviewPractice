"""
>>> add_binary("0","0")
'0'
>>> add_binary("0","1")
'1'
>>> add_binary("1","0")
'1'
>>> add_binary("1","1")
'10'
>>> add_binary("1010","101")
'1111'
>>> add_binary("1111","1")
'10000'
"""


def add_binary(a, b):
    """ Add Binary """

    a_len = len(a)
    b_len = len(b)

    offset = a_len - b_len

    max_len = a_len
    if offset > 0:
        b = "0"*offset + b
        max_len = a_len
    elif offset < 0:
        a = "0"*-offset + a
        max_len = b_len

    carryover = 0
    c = ""
    for idx in range(max_len):
        rev_idx = max_len - idx - 1
        a_val = a[rev_idx]
        b_val = b[rev_idx]
        if a_val == "1" and b_val == "1":
            if carryover == 1:
                c = "1" + c
            else:
                c = "0" + c
            carryover = 1
        elif (a_val == "1" and b_val == "0") or \
             (a_val == "0" and b_val == "1"):
            if carryover == 1:
                c = "0" + c
                carryover = 1
            else:
                c = "1" + c
                carryover = 0
        else:
            if carryover == 1:
                c = "1" + c
                carryover = 0
            else:
                c = "0" + c

    if carryover == 1:
        c = "1" + c

    return c