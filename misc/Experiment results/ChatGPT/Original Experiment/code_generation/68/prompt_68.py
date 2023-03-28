def pluck(arr):
    if not arr:
        return []
    min_val = float('inf')
    min_index = float('inf')
    for i, x in enumerate(arr):
        if x % 2 == 0 and x < min_val:
            min_val = x
            min_index = i
    if min_val == float('inf'):
        return []
    return [min_val, min_index]
