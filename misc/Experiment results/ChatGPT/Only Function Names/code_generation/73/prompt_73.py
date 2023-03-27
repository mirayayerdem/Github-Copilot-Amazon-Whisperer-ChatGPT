
def smallest_change(arr):
    arr.sort() # sort the input list
    min_diff = float('inf') # initialize a variable to store the minimum difference with positive infinity
    for i in range(1, len(arr)): # start at index 1 to compare each element with the one before it
        min_diff = min(min_diff, arr[i] - arr[i-1])
    return min_diff
