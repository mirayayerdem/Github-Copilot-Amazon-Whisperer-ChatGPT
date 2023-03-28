def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def prime_fib(n: int):
    a, b = 0, 1  # Initialize first two Fibonacci numbers
    count = 0  # Initialize count to 0
    while count < n:  # Repeat until count reaches n
        a, b = b, a + b  # Generate next Fibonacci number
        if is_prime(b):  # Check if b is prime
            count += 1  # Increment count
    return b
