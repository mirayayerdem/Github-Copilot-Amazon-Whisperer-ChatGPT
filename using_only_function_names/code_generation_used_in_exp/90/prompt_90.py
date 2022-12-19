
def next_smallest(lst):
    """
    This function takes a list of integers and returns the next smallest
    integer in the list.
    """
    if len(lst) == 0:
        return None
    else:
        min_index = 0
        for i in range(1, len(lst)):
            if lst[i] < lst[min_index]:
                min_index = i
        return min_index
