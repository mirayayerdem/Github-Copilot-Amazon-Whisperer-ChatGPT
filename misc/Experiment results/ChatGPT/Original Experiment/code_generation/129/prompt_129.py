def minPath(grid, k):
    n = len(grid)
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    visited = [[False for _ in range(n)] for _ in range(n)]
    heap = [(grid[0][0], 0, 0)]
    while heap:
        curr, x, y = heapq.heappop(heap)
        if visited[x][y]:
            continue
        visited[x][y] = True
        k -= 1
        if k == 0:
            return curr
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n:
                heapq.heappush(heap, (grid[nx][ny], nx, ny))
    return []
