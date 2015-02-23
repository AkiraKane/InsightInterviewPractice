"""
>>> get_row(3)
[1, 3, 3, 1]
>>> get_row(5)
[1, 5, 10, 10, 5, 1]
"""

def get_row(rowIndex):
    """ Pascal's Triangle II """

    rowIndex += 1

    for i in range(rowIndex):
        if i == 0:
            tri = [1]
        elif i == 1:
            tri.append(1)
        else:
            last_val = tri[0]
            for j in range(len(tri)-1):
                new_val = last_val + tri[j+1]
                last_val = tri[j+1]
                tri[j+1] = new_val
            tri.append(last_val)

    return tri


if __name__ == "__main__":
    import doctest
    doctest.testmod()