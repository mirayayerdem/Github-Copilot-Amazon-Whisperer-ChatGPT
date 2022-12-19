
def max_fill(grid, capacity):
    row_count = len(grid)
    col_count = len(grid[0])
    max_height = 0
    for row in range(row_count):
        for col in range(col_count):
            if grid[row][col] > capacity:
                continue
            height = 0
            while row < row_count and col < col_count:
                height += grid[row][col]
                if height > capacity:
                    break
                row += 1
                col += 1
            if height > max_height:
                max_height = height
    return max_height