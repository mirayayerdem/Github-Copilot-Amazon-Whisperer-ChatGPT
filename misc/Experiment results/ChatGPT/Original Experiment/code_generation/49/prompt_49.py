def modp(n: int, p: int):
    # Initialize result to 1
    result = 1
    # Initialize base to 2
    base = 2
    # Repeat until n becomes zero
    while n > 0:
        # If n is odd, multiply result by base
        if n % 2 == 1:
            result = (result * base) % p
        # Divide n by 2
        n = n // 2
        # Square base
        base = (base * base) % p
    return result
