from collections import deque

def minPath(grid, k):
    rows = len(grid)
    cols = len(grid[0])
    q = deque()
    q.append((0, 0, k))
    visited = set()
    while q:
        row, col, k = q.popleft()
        if (row, col, k) in visited:
            continue
        visited.add((row, col, k))
        if row == rows - 1 and col == cols - 1:
            return grid[row][col]
        for r, c in [(row, col + 1), (row + 1, col)]:
            if r < rows and c < cols:
                cost = grid[r][c] - grid[row][col]
                if cost <= k:
                    q.append((r, c, k - cost))
                else:
                    q.append((r, c, k))
    return -1
