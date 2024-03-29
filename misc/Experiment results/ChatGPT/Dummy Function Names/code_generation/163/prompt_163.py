
def foo(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    foo(2, 8) => [2, 4, 6, 8]
    foo(8, 2) => [2, 4, 6, 8]
    foo(10, 14) => []
    """
    if a > b:
        a, b = b, a
    return sorted([x for x in range(a, b+1) if x % 2 == 0])
