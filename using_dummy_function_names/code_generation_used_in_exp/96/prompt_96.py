
def foo(n):
    """Implement a function that takes an non-negative integer and returns an array of the first n
    integers that are prime numbers and less than n.
    for example:
    foo(5) => [2,3]
    foo(11) => [2,3,5,7]
    foo(0) => []
    foo(20) => [2,3,5,7,11,13,17,19]
    foo(1) => []
    foo(18) => [2,3,5,7,11,13,17]
    """
    return [x for x in range(2, n) if all(x % y != 0 for y in range(2, x))]
