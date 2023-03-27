

import math

def is_prime(n: int) -> bool:
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    for i in range(5, int(math.sqrt(n)) + 1):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True

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
    count = 0
    fib = [0,1]
    while count != n:
        fib.append(fib[-1] + fib[-2])
        if is_prime(fib[-1]):
            count += 1
    return fib[-1]
