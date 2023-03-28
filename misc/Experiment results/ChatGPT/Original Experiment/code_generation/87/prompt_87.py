def get_row(lst, x):
    result = []
    for i, row in enumerate(lst):
        for j, value in enumerate(row):
            if value == x:
                result.append((i, j))
    result.sort(key=lambda coord: (coord[0], -coord[1]))
    return result
