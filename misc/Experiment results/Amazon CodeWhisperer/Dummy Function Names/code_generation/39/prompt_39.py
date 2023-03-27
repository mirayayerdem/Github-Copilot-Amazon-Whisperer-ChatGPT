

def foo(n: int):
    """
    prime_fib returns n-th number that is a Fibonacci number and it's also prime.
    >>> foo(1)
    2
    >>> foo(2)
    3
    >>> foo(3)
    5
    >>> foo(4)
    13
    >>> foo(5)
    89
    """
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a
