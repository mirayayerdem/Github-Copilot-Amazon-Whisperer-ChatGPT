
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
    if len(arr) == 0:
        return None
    else:
        product = 1
        sum_of_magnitude = 0
        for number in arr:
            if number != 0:
                sum_of_magnitude += abs(number)
                product *= (1 if number > 0 else -1)
        return sum_of_magnitude * product
