"""
>>> board = ["OOO","OOO","OOO"]
>>> solve(board)
>>> print board
['OOO', 'OOO', 'OOO']
>>> print board[0]
OOO
"""


def solve(board):
    """ Surrounded Regions """
    # search for "O" on border
    # replace any neighboring "O" with "P"
    # iterate until end of perimeter
    # replace all "O" with "X"
    # replace all "P" with "O"

    # minimum size has to be 3 by 3
    m = len(board)
    if m <= 2:
        return

    n = len(board[0])
    if n <= 2:
        return

    def tag_non_enclosed(board_in, curr_x, curr_y):
        board_in[curr_x][curr_y] = "P"

        try:
            # check if you can move down
            if curr_x-1 >= 0:
                if board_in[curr_x-1][curr_y] == "O":
                    tag_non_enclosed(board_in, curr_x-1, curr_y)
        except:
            pass

        try:
            # check if you can move up
            if curr_x+1 < len(board_in):
                if board_in[curr_x+1][curr_y] == "O":
                    tag_non_enclosed(board_in, curr_x+1, curr_y)
        except:
            pass

        try:
            # check if you can move left
            if curr_y-1 >= 0:
                if board_in[curr_x][curr_y-1] == "O":
                    tag_non_enclosed(board_in, curr_x, curr_y-1)
        except:
            pass

        try:
            # check if you can move right
            if curr_y+1 < len(board_in[0]):
                if board_in[curr_x][curr_y+1] == "O":
                    tag_non_enclosed(board_in, curr_x, curr_y+1)
        except:
            pass

    m_border = range(0, m)
    n_border = range(0, n)
    mn_border = [0, m-1, n-1, 0]

    board[:] = [list(a) for a in board]

    for border, mn_val in enumerate(mn_border):
        # iterate on top, right, bottom, left border
        along_m = border % 2 != 0
        if along_m:
            x = mn_val
            for y in n_border:
                if board[x][y] == "O":
                    tag_non_enclosed(board, x, y)
        else:
            y = mn_val
            for x in m_border:
                if board[x][y] == "O":
                    tag_non_enclosed(board, x, y)

    for m_ind in range(m):
        for n_ind in range(n):
            if board[m_ind][n_ind] == "O":
                board[m_ind][n_ind] = "X"
            elif board[m_ind][n_ind] == "P":
                board[m_ind][n_ind] = "O"

    board[:] = ["".join(a) for a in board]

