

def prime_fib(n: int):
    """
    Returns the nth prime number in the Fibonacci sequence.
    """
    if n < 1:
        raise ValueError("n must be greater than 0.")

    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a
