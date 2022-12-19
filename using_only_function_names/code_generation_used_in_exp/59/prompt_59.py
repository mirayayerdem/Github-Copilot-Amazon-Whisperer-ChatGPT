

def largest_prime_factor(n: int):
    """
    Calculates the largest prime factor of a number.
    :param n: number to calculate the largest prime factor of.
    :return: largest prime factor of n.
    """
    if n == 1:
        return 1
    for i in range(2, n):
        if n % i == 0:
            return largest_prime_factor(n / i)
    return n
