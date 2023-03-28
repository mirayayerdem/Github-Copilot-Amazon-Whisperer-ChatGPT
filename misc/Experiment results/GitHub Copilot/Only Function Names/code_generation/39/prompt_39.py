

def prime_fib(n: int):
    """Return the nth prime Fibonacci number.

    Precondition: n >= 1

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

    def is_prime(n: int) -> bool:
        """Return True if n is prime, and False otherwise.

        Precondition: n >= 2

        >>> is_prime(2)
        True
        >>> is_prime(3)
        True
        >>> is_prime(4)
        False
        >>> is_prime(5)
        True
        >>> is_prime(6)
        False
        >>> is_prime(7)
        True
        >>> is_prime(8)
        False
        >>> is_prime(9)
        False
        >>> is_prime(10)
        False
        >>> is_prime(11)
        True
        >>> is_prime(12)
        False
        >>> is_prime(13)
        True
        """

        i = 2
        while i < n:
            if n % i == 0:
                return False
            i += 1
        return True

    def fib(n: int) -> int:
        """Return the nth Fibonacci number.

        Precondition: n >= 1

        >>> fib(1)
        1
        >>> fib(2)
        1
        >>> fib(3)
        2
        >>> fib(4)
        3
        >>> fib(5)
        5
        >>> fib(6)
        8
        >>> fib(7)
        13
        """

        if n == 1 or n == 2:
            return 1
        else:
            return fib(n - 1) + fib(n - 2)

    i = 1
    count = 0
    while count < n:
        if is_prime(fib(i)):
            count += 1
        i += 1
    return fib(i - 1)