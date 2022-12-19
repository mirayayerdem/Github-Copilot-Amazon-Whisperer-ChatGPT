

def sort_third(l: list):
    """
    Sorts a list of lists by the third element in the sublists.
    :param l: List of lists.
    :return: Sorted list of lists.
    """
    return sorted(l, key=lambda x: x[2])
