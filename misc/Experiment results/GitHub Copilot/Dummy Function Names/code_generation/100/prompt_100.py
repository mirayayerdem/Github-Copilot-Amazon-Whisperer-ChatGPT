
def foo(n):
    """
    Given a positive integer n, you have to make a pile of n levels of stones.
    The first level has n stones.
    The number of stones in the next level is:
        - the next odd number if n is odd.
        - the next even number if n is even.
    Return the number of stones in each level in a list, where element at index
    i represents the number of stones in the level (i+1).

    Examples:
    >>> foo(3)
    [3, 5, 7]
    """
    if n == 1:
        return [1]
    else:
        return [n] + foo(n + 2 if n % 2 == 1 else n + 1)
