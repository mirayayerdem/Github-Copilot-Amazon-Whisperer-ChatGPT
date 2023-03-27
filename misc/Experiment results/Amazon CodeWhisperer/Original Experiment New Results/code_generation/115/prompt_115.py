
def max_fill(grid, capacity):
    import math
    """
    You are given a rectangular grid of wells. Each row represents a single well,
    and each 1 in a row represents a single unit of water.
    Each well has a corresponding bucket that can be used to extract water from it, 
    and all buckets have the same capacity.
    Your task is to use the buckets to empty the wells.
    Output the number of times you need to lower the buckets.

    Example 1:
        Input: 
            grid : [[0,0,1,0], [0,1,0,0], [1,1,1,1]]
            bucket_capacity : 1
        Output: 6

    Example 2:
        Input: 
            grid : [[0,0,1,1], [0,0,0,0], [1,1,1,1], [0,1,1,1]]
            bucket_capacity : 2
        Output: 5
    
    Example 3:
        Input: 
            grid : [[0,0,0], [0,0,0]]
            bucket_capacity : 5
        Output: 0

    Constraints:
        * all wells have the same length
        * 1 <= grid.length <= 10^2
        * 1 <= grid[:,1].length <= 10^2
        * grid[i][j] -> 0 | 1
        * 1 <= capacity <= 10
    """
    if not grid:
        return 0

    n = len(grid)
    m = len(grid[0])
    dp = [[0 for _ in range(m)] for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 1:
                dp[i][j] = 0
            else:
                dp[i][j] = math.inf
                for j in range(m):
            if grid[i][j] == 1:
                dp[i][j] = -math.inf
            else:
                if i == 0:
                    dp[i][j] = 0
                else:
                    dp[i][j] = dp[i-1][j] + 1
                    for k in range(1, m):
                        for k in range(j):
                            for k in range(j+1, m):
                                if grid[i][k] == 1:
                            dp[i][j] = min(dp[i][j], dp[i-1][k-1] + 1)
                            if j - k >= 0:
                            dp[i][j] = min(dp[i][j], dp[i-1][j-k] + 1)
                        else:
                            break
                        if dp[i][j] == 0:
                            break

    return dp[n-1][m-1]

    