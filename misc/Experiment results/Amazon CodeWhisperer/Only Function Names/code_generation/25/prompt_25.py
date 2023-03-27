from typing import List


def factorize(n: int) -> List[int]:
    """
    Factorize positive integer and return its factors.
    :param n: positive integer
    :return: list of factors
    """
    factors = []
    for i in range(1, n + 1):
        if n % i == 0:
            factors.append(i)
    return factors