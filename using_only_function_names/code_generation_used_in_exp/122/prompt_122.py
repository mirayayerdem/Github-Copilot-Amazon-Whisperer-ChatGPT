
def add_elements(arr, k):
    """
    Given a list of integers, return a list of the integers that appear more than once.
    """
    return [x for x in arr if arr.count(x) > 1]



