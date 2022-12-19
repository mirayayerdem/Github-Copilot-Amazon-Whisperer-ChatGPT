
def smallest_change(arr):
    """
    Finds the smallest change that can be made with the given coins.
    :param arr: List of coins.
    :return: Smallest change.
    """
    if len(arr) == 1:
        return arr[0]
    else:
        return min(arr[0] + smallest_change(arr[1:]), arr[1] + smallest_change(arr[2:]))

