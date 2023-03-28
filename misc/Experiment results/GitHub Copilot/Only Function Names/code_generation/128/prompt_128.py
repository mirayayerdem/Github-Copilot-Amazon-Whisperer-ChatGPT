
def prod_signs(arr):
    """ (list of int) -> int
    Return the product of the signs of the elements in arr.
    """
    return reduce(lambda x, y: x * y, [i / abs(i) for i in arr])