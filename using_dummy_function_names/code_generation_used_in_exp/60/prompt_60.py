

def foo(n: int):
    """foo is a function that sums numbers from 1 to n.
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
    if n == 0:
        return 0
    else:
        return n + foo(n - 1)
