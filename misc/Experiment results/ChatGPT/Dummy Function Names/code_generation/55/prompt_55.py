

def foo(n: int):
    """Return n-th Fibonacci number.
    >>> foo(10)
    55
    >>> foo(1)
    1
    >>> foo(8)
    21
    """
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n+1):
            c = a + b
            a, b = b, c
        return b
 
