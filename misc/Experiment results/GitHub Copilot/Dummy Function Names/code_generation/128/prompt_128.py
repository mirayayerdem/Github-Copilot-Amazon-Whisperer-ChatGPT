
def foo(arr):
    """
    You are given an array arr of integers and you need to return
    sum of magnitudes of integers multiplied by product of all signs
    of each number in the array, represented by 1, -1 or 0.
    Note: return None for empty arr.

    Example:
    >>> foo([1, 2, 2, -4]) == -9
    >>> foo([0, 1]) == 0
    >>> foo([]) == None
    """
    if not arr:
        return None
    return sum([abs(x) for x in arr]) * reduce(lambda x, y: x*y, [1 if x > 0 else -1 if x < 0 else 0 for x in arr])
