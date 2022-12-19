from typing import List


def factorize(n: int) -> List[int]:
    """
    Factorizes a number.
    :param n: Number to factorize.
    :return: List of factors.
    """
    factors = []
    for i in range(1, n + 1):
        if n % i == 0:
            factors.append(i)
    return factors
