"""
>>> spiral_order([[1, 2, 3, 4, 5],
...               [20, 21, 22, 23, 6],
...               [19, 32, 33, 24, 7],
...               [18, 31, 34, 25, 8],
...               [17, 30, 35, 26, 9],
...               [16, 29, 28, 27, 10],
...               [15, 14, 13, 12, 11]])
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, \
22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]
>>> spiral_order([[1, 2, 3, 4, 5],
...               [10, 9, 8, 7, 6]])
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> spiral_order([[1, 2],
...               [10, 3],
...               [9, 4],
...               [8, 5],
...               [7, 6]])
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> spiral_order([[1, 2, 3, 4, 5]])
[1, 2, 3, 4, 5]
>>> spiral_order([[1],
...               [2],
...               [3],
...               [4],
...               [5]])
[1, 2, 3, 4, 5]
>>> spiral_order([[3], [2]])
[3, 2]
>>> spiral_order([[5]])
[5]
>>> spiral_order([[]])
[]
>>> spiral_order([])
[]
"""


def spiral_order(matrix):
    """ Spiral Matrix """

    cnt = 0
    m = len(matrix)
    if m == 0:
        return []
    n = len(matrix[0])
    if n == 0:
        return []
    if m == 1 and n == 1:
        return [matrix[0][0]]

    x = 0
    y = 0
    inc_x = True
    inc_y = True
    trav_y = True
    x_up_to = m-1
    y_up_to = n-1
    x_down_to = 1
    y_down_to = 0
    sp = []
    while cnt < m*n:
        if trav_y:
            if inc_y:
                if y < y_up_to:
                    sp.append(matrix[x][y])
                    y += 1
                    cnt += 1
                else:
                    y_up_to -= 1
                    inc_y = not inc_y
                    trav_y = not trav_y

            else:
                if y > y_down_to:
                    sp.append(matrix[x][y])
                    y -= 1
                    cnt += 1
                else:
                    y_down_to += 1
                    inc_y = not inc_y
                    trav_y = not trav_y

        else:
            if inc_x:
                if x < x_up_to:
                    sp.append(matrix[x][y])
                    x += 1
                    cnt += 1
                else:
                    x_up_to -= 1
                    inc_x = not inc_x
                    trav_y = not trav_y
            else:
                if x > x_down_to:
                    sp.append(matrix[x][y])
                    x -= 1
                    cnt += 1
                else:
                    x_down_to += 1
                    inc_x = not inc_x
                    trav_y = not trav_y

    return sp


if __name__ == "__main__":
    import doctest
    doctest.testmod()
