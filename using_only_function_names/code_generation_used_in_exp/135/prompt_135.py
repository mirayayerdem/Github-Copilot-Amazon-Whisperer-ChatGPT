
def can_arrange(arr):
    """
    Given an array of integers, return True if it can be arranged into a
    sequence of consecutive numbers.
    """
    return sorted(arr) == list(range(min(arr), max(arr) + 1))

