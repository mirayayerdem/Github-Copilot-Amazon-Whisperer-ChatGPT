
def foo(arr):
    """
    Write a function foo which takes an array of integers and returns
    the number of elements which has a sum of digits > 0.
    If a number is negative, then its first signed digit will be negative:
    e.g. -123 has signed digits -1, 2, and 3.
    >>> foo([]) == 0
    >>> foo([-1, 11, -11]) == 1
    >>> foo([1, 1, 2]) == 3
    """
    return sum(1 for x in arr if x > 0 and sum(int(i) for i in str(abs(x))) > 0)
