"""
>>> grid = [[0, 0, 0],
...         [0, 1, 0],
...         [0, 0, 0]]
>>> unique_paths_with_obstacles(grid)
2
"""

memo = {}


def unique_paths_with_obstacles(obstacle_grid):
    """ Unique Paths With Obstacles """

    def unique_paths(m, n):

        if obstacle_grid[m-1][n-1] == 1:
            return 0

        if m == 1 and n == 1:
            return 1

        if m == 1:
            if (m, n-1) not in memo:
                memo[(m, n-1)] = unique_paths(m, n-1)
            return memo[(m, n-1)]
        elif n == 1:
            if (m-1, n) not in memo:
                memo[(m-1, n)] = unique_paths(m-1, n)
            return memo[(m-1, n)]
        else:
            if (m, n-1) not in memo:
                memo[(m, n-1)] = unique_paths(m, n-1)

            if (m-1, n) not in memo:
                memo[(m-1, n)] = unique_paths(m-1, n)

            return memo[(m, n-1)] + memo[(m-1, n)]

    m_grid, n_grid = len(obstacle_grid), len(obstacle_grid[0])
    return unique_paths(m_grid, n_grid)

