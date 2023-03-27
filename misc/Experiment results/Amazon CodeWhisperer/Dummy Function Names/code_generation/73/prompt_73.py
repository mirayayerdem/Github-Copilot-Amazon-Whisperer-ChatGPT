
def foo(arr):
    """
    Given an array arr of integers, find the minimum number of elements that
    need to be changed to make the array palindromic. A palindromic array is an array that
    is read the same backwards and forwards. In one change, you can change one element to any other element.

    For example:
    foo([1,2,3,5,4,7,9,6]) == 4
    foo([1, 2, 3, 4, 3, 2, 2]) == 1
    foo([1, 2, 3, 2, 1]) == 0
    """
    if not arr:
        return 0
    if len(arr) == 1:
        return 0
    if arr[0] != arr[-1]:
        return 1
    return foo(arr[1:-1])
