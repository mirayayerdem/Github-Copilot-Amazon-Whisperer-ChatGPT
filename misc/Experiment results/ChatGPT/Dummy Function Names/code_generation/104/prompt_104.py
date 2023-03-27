
def foo(x):
    """Given a list of positive integers x. return a sorted list of all 
    elements that hasn't any even digit.

    Note: Returned list should be sorted in increasing order.
    
    For example:
    >>> foo([15, 33, 1422, 1])
    [1, 15, 33]
    >>> foo([152, 323, 1422, 10])
    []
    """
    def has_even_digit(num):
        for digit in str(num):
            if int(digit) % 2 == 0:
                return True
        return False

    return sorted([i for i in x if not has_even_digit(i)])
