

def sort_even(l: list):
    """
    Sorts a list of numbers by the even numbers.
    :param l: List of numbers.
    :return: Sorted list of numbers.
    """
    return sorted(l, key=lambda x: x % 2 == 0)
