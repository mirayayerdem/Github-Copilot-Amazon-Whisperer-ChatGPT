
def max_fill(grid, capacity):
    rows = len(grid)
    cols = len(grid[0])
    filled = 0
    for row in range(rows):
        for col in range(cols):
            if grid[row][col] < capacity:
                filled += capacity - grid[row][col]
                grid[row][col] = capacity
    return filled
