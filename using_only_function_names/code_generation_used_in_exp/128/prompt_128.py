
def prod_signs(arr):
    """
    Given an array of integers, return the product of the integers that have
    the same sign.
    """
    return sum([x for x in arr if x > 0]) * sum([x for x in arr if x < 0])

