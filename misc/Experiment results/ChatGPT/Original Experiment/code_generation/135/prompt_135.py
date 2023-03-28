def can_arrange(arr):
    max_index = -1
    for i in range(1, len(arr)):
        if arr[i] < arr[i-1]:
            max_index = i
    return max_index
