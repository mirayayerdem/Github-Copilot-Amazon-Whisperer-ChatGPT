
def is_equal_to_sum_even(n):
    """
    Returns True if n is an even-odd palindrome.
    :param n: Number.
    :return: True if n is an even-odd palindrome.
    """
    return n % 2 == 0 and str(n) == str(n)[::-1]
