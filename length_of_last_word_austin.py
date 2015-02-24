"""
>>> length_of_last_word("Hello")
5
>>> length_of_last_word(" Hello")
5
>>> length_of_last_word("Hello ")
5
>>> length_of_last_word(" Hello ")
5
>>> length_of_last_word("He l lo00 ")
4
"""


def length_of_last_word(s):
    """ Length of Last Word """

    space_idx = None

    space_from_end = True
    num_spaces_from_end = 0

    for idx in range(len(s)):
        rev_idx = len(s)-idx-1
        if s[rev_idx] == " ":
            if space_from_end:
                num_spaces_from_end += 1
            else:
                space_idx = rev_idx
                return len(s) - space_idx - num_spaces_from_end - 1

        else:
            space_from_end = False

    if space_idx is None:
        return len(s) - num_spaces_from_end