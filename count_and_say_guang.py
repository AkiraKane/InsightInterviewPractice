def count_and_say(n):
    """ computes nth element in the sequence of count-and-say
    numbers.

    Args:
        n: how many elements should be in the sequence

    Returns:
        nth_elt: resulting element in count-and-say sequence

    Examples:
    >>> count_and_say(0)
    '1'
    >>> count_and_say(1)
    '11'
    >>> count_and_say(2)
    '21'
    >>> count_and_say(3)
    '1211'
    >>> count_and_say(4)
    '111221'
    """

    if n == 0:
        return '1'
    else:
        raw = count_and_say(n-1)
        return say(raw)


def say(raw_str):
    """ say a given raw string

    partition into substrings that have identical elements
    get (len, val) pair for each substring
    concatenate the resulting (len, val) pairs

    Examples:
    >>> say('11')
    '21'
    >>> say('21')
    '1211'
    >>> say('1211')
    '111221'
    """

    if len(raw_str) == 1:
        return '11'
    else:
        curr_len = 1
        len_val_pairs = []
        raw_str = raw_str + ' '     # appends space at end
        for ind in range(1, len(raw_str)):
            val = raw_str[ind]
            prev_val = raw_str[ind-1]
            if val == prev_val:
                curr_len += 1
            else:
                len_val_pairs.append(str(curr_len))
                len_val_pairs.append(prev_val)
                curr_len = 1
        return ''.join(len_val_pairs)
