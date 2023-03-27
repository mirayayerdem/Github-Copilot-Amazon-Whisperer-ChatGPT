def foo(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the indicies that are not divisible by three, while its values at the indicies that are divisible by three are equal
    to the values of the corresponding indicies of l, but sorted.
    >>> foo([1, 2, 3])
    [1, 2, 3]
    >>> foo([5, 6, 3, 4, 8, 9, 2])
    [2, 6, 3, 4, 8, 9, 5]
    """
    l_prime = list(l)
    for i in range(0, len(l), 3):
        l_prime[i:i+3] = sorted(l[i:i+3])
    return l_prime

