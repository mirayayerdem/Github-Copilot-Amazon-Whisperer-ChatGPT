
def foo(grid, capacity):
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
    # Time complexity: O(N^2)
    # Space complexity: O(N^2)
    # N = len(grid)
    # buckets = [[0] * N for _ in range(N)]
    # for i in range(N):
    #     for j in range(N):
    #         if grid[i][j] == 1:
    #             buckets[i][j] = capacity
    #         else:
    #             buckets[i][j] = 0
    # count = 0
    # while True:
    #     flag = True
    #     for i in range(N):
    #         for j in range(N):
    #             if buckets[i][j] > 0:
    #                 flag = False
    #                 break
    #         if not flag:
    #             break
    #     if flag:
    #         break
    #     count += 1
    #     for i in range(N):
    #         for j in range(N):
    #             if buckets[i][j] > 0:
    #                 buckets[i][j] -= 1
    #                 if i + 1 < N:
    #                     buckets[i + 1][j] += 1
    #                 if j + 1 < N:
    #                     buckets[i][j + 1] += 1
    # return count
    
