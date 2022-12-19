
def is_multiply_prime(a):
    """
    Checks if a number is a multiply prime.
    :param a: number to check.
    :return: True if a is a multiply prime, False otherwise.
    """
    for i in range(2, a):
        if a % i == 0:
            return False
    return True

