
def minPath(grid, k):
    """
    Given a grid of integers, find the minimum path sum from top left to bottom right.
    """
    row_count = len(grid)
    col_count = len(grid[0])
    for row in range(row_count - 1, -1, -1):
        for col in range(col_count - 1, -1, -1):
            if row == row_count - 1 and col == col_count - 1:
                continue
            if row == row_count - 1:
                grid[row][col] += grid[row][col + 1]
            elif col == col_count - 1:
                grid[row][col] += grid[row + 1][col]
            else:
                grid[row][col] += min(grid[row + 1][col], grid[row][col + 1])
    return grid[0][0]

    




