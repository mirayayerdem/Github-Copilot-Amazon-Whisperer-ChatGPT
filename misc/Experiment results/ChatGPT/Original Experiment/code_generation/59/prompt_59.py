def largest_prime_factor(n: int):
    # Divide by 2 as many times as possible
    while n % 2 == 0:
        n = n // 2

    # n is now odd
    largest_factor = n

    # Divide by the next prime numbers (3, 5, 7, etc.)
    factor = 3
    while n > 1:
        while n % factor == 0:
            n = n // factor
            largest_factor = factor
        factor += 2

    return largest_factor
