
def foo(array):
    """
    Given an array of non-negative integers, return a copy of the given array after sorting,
    you will sort the given array in ascending order if the sum( first index value, last index value) is odd,
    or sort it in descending order if the sum( first index value, last index value) is even.

    Note:
    * don't change the given array.

    Examples:
    * foo([]) => []
    * foo([5]) => [5]
    * foo([2, 4, 3, 0, 1, 5]) => [0, 1, 2, 3, 4, 5]
    * foo([2, 4, 3, 0, 1, 5, 6]) => [6, 5, 4, 3, 2, 1, 0]
    """
    return sorted(array, key=lambda x: x[0] + x[-1], reverse=sum(x[0] + x[-1]) % 2)
