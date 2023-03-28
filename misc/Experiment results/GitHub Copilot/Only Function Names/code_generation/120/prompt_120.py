
def maximum(arr, k):
    """ (list of int, int) -> int
    Return the maximum value in arr that is less than or equal to k.
    """
    return max(i for i in arr if i <= k)