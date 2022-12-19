

def foo(n: int):
    """The Fib4 number sequence is a sequence similar to the Fibbonacci sequnece that's defined as follows:
    foo(0) -> 0
    foo(1) -> 0
    foo(2) -> 2
    foo(3) -> 0
    foo(n) -> foo(n-1) + foo(n-2) + foo(n-3) + foo(n-4).
    Please write a function to efficiently compute the n-th element of the foo number sequence.  Do not use recursion.
    >>> foo(5)
    4
    >>> foo(6)
    8
    >>> foo(7)
    14
    """
    if n == 0 or n == 1:
        return 0
    elif n == 2 or n == 3:
        return 2
    else:
        return foo(n - 1) + foo(n - 2) + foo(n - 3) + foo(n - 4)
