
def is_sorted(lst):
    """
    Returns True if the list is sorted in descending order.
    """
    return all(lst[i] >= lst[i + 1] for i in range(len(lst) - 1))

