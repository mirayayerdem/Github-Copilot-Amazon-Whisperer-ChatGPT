
def is_happy(s):
    """ (str) -> bool

    Return True if and only if s is a happy number.

    >>> is_happy('7')
    True
    >>> is_happy('10')
    True
    >>> is_happy('13')
    True
    >>> is_happy('19')
    True
    >>> is_happy('20')
    False
    """

    # The digits of s.
    digits = [int(c) for c in s]

    # Keep replacing s with the sum of the squares of its digits,
    # until s is 1 or we get stuck in a cycle.
    while s != '1' and s != '4':
        s = str(sum(d ** 2 for d in digits))
        digits = [int(c) for c in s]

    return s == '1'