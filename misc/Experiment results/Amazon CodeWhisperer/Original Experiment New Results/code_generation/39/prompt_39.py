

def prime_fib(n: int):
    """
    prime_fib returns n-th number that is a Fibonacci number and it's also prime.
    >>> prime_fib(1)
    2
    >>> prime_fib(2)
    3
    >>> prime_fib(3)
    5
    >>> prime_fib(4)
    13
    >>> prime_fib(5)
    89
    """
    a, b = 1, 2
    while True:
        if is_prime(b) and is_fibonacci(b):
            if n == 1:
                return b
            n -= 1
        a, b = b, a + b


def is_prime(n: int):
    """
    is_prime returns True if n is prime.
    >>> is_prime(2)
    True
    >>> is_prime(3)
    True
    >>> is_prime(4)
    False
    >>> is_prime(5)
    True
    """
    if n == 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def is_fibonacci(n: int):
    """
    is_fibonacci returns True if n is a Fibonacci number.
    >>> is_fibonacci(2)
    False
    >>> is_fibonacci(3)
    True
    >>> is_fibonacci(4)
    True
    >>> is_fibonacci(5)
    False
    """
    a, b = 0, 1
    while a < n:
        a, b = b, a + b
    return a == n
