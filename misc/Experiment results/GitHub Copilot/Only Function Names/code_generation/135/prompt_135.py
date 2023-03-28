
def can_arrange(arr):
    """ (list of int) -> bool
    Return True if and only if the elements of arr can be arranged in
    ascending order.
    """
    return sorted(arr) == arr