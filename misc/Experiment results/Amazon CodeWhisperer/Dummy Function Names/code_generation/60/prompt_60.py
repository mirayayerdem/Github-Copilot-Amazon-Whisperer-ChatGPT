

def foo(n: int):
    """sum_to_n is a function that sums numbers from 1 to n.
    >>> foo(30)
    465
    >>> foo(100)
    5050
    >>> foo(5)
    15
    >>> foo(10)
    55
    >>> foo(1)
    1
    """
    if n == 1:
        return 1
    else:
        return n + foo(n-1)
