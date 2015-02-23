"""
>>> title_to_number("A")
1
>>> title_to_number("Z")
26
>>> title_to_number("AA")
27
>>> title_to_number("AAA")
703
"""


def map_chr_to_int(char_in):
    return ord(char_in)-64


def title_to_number(s):
    """ Excel Sheet Column Number """

    if len(s) == 0:
        return 0

    tot_sum = map_chr_to_int(s[0])*26**(len(s)-1)
    return tot_sum + title_to_number(s[1:])


if __name__ == "__main__":
    import doctest
    doctest.testmod()