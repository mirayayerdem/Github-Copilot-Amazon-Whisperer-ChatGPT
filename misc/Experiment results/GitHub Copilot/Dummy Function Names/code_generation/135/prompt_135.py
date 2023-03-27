
def foo(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    foo([1,2,4,3,5]) = 3
    foo([1,2,3]) = -1
    """
    return max([i for i in range(len(arr)) if arr[i] < arr[i-1]], default=-1)
