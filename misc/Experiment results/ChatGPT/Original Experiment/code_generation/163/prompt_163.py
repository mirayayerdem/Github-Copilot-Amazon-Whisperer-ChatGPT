def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """
    # make sure a is always smaller than b
    if a > b:
        a, b = b, a
    # create an empty list to store the even digits
    even_digits = []
    for i in range(a, b+1):
        if i % 2 == 0:
            even_digits.append(i)
    return even_digits
