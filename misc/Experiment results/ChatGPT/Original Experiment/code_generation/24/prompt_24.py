def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    """
    # Iterate through the numbers from n - 1 down to 1
    for i in range(n - 1, 1, -1):
        # If n is divisible by i, return i
        if n % i == 0:
            return i
    # If no divisor is found, return 1
    return 1
