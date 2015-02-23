"""
>>> generate(5)
[[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
"""


def generate(num_rows):
    """ Pascal's Triangle """

    tri = []
    for i in range(num_rows):
        if i == 0:
            tri.append([1])
        elif i == 1:
            tri.append(tri[i-1] + [1])
        else:
            prev_tri = tri[i-1]
            new_tri = [1]
            for k in range(len(prev_tri)-1):
                new_tri.append(prev_tri[k] + prev_tri[k+1])
            new_tri.append(1)
            tri.append(new_tri)

    return tri


if __name__ == "__main__":
    import doctest
    doctest.testmod()