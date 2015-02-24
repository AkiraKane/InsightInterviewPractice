"""
>>> num = [1,2,3,4,5,6,7]
>>> rotate(num, 3)
>>> print num
[5, 6, 7, 1, 2, 3, 4]
>>> num = [1,2,3,4,5,6,7]
>>> rotate(num, 7)
>>> print num
[1, 2, 3, 4, 5, 6, 7]
>>> num = [1]
>>> rotate(num, 3)
>>> print num
[1]
>>> num = []
>>> rotate(num, 3)
>>> print num
[]
>>> num = [1, 2, 3, 4, 5, 6]
>>> rotate(num, 2)
>>> print num
[5, 6, 1, 2, 3, 4]
"""


def rotate(nums, k):
    """ Rotate Array """
    num_len = len(nums)
    if num_len <= 1:
        return

    offset = 0
    idx = (offset + k) % num_len
    for rep in range(num_len-1):

        nums[idx], nums[offset] = nums[offset], nums[idx]
        prev_idx = idx

        if prev_idx == offset:
            offset += 1
            idx = offset
        idx = (idx + k) % num_len


if __name__ == "__main__":
    import doctest
    doctest.testmod()