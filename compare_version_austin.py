"""
>>> compare_version("0.1", "1.1")
-1
>>> compare_version("1.2", "1.1")
1
>>> compare_version("13.37", "13")
1
>>> compare_version("1.2.3.4", "1.2.3.70")
-1
>>> compare_version("1.2.3.4", "1.2.3.4")
0
"""


def compare_version(version1, version2):
    """ Compare Version Numbers """

    split_ver1 = map(lambda x: int(x), version1.split("."))
    split_ver2 = map(lambda x: int(x), version2.split("."))

    ver1_len = len(split_ver1)
    ver2_len = len(split_ver2)

    if ver1_len > ver2_len:
        split_ver2 += [0]*(ver1_len-ver2_len)
    elif ver2_len > ver1_len:
        split_ver1 += [0]*(ver2_len-ver1_len)

    for ver1, ver2 in zip(split_ver1, split_ver2):
        if ver1 > ver2:
            return 1
        elif ver2 > ver1:
            return -1

    return 0


if __name__ == "__main__":
    import doctest
    doctest.testmod()