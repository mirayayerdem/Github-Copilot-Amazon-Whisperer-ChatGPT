
def maximum(arr, k):
    n = len(arr)
    max_sum = 0
    for i in range(n-k+1):
        max_sum = max(max_sum, sum(arr[i:i+k]))
    return max_sum







