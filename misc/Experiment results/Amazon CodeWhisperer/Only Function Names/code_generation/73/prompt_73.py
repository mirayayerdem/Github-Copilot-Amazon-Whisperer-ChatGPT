
def smallest_change(arr):
    arr.sort()
    min_change = 0
    for i in range(len(arr)):
        min_change += arr[i]
    return min_change
