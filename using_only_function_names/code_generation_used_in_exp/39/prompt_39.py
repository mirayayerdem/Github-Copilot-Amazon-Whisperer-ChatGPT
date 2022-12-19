

def prime_fib(n: int):
    """
    Calculates the nth prime number.
    :param n: nth prime number.
    :return: nth prime number.
    """
    if n == 1:
        return 2
    elif n == 2:
        return 3
    else:
        a = 2
        b = 3
        for i in range(3, n):
            c = a + b
            a = b
            b = c
            if is_prime(c):
                return c
