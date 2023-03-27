
def is_sorted(lst):
    """Returns True if the list is sorted in ascending order, and False otherwise."""
    for i in range(len(lst) - 1):
        if lst[i] > lst[i + 1]:
            return False
    return True

