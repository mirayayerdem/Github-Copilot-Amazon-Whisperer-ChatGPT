
def search(lst):
    """
    This function takes a list of integers and returns the index of the
    largest integer in the list.
    """
    if len(lst) == 0:
        return None
    else:
        max_index = 0
        for i in range(1, len(lst)):
            if lst[i] > lst[max_index]:
                max_index = i
        return max_index
