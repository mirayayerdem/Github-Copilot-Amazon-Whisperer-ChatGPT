

def sort_third(l: list):
    """
    Sorts the third element of the list.
    """
    l.sort(key=lambda x: x[2])
    return l