

def common(l1: list, l2: list):
    """
    Returns the common elements of two lists.
    :param l1: List of elements.
    :param l2: List of elements.
    :return: List of common elements.
    """
    return list(set(l1) & set(l2))

