
def foo(lst):
    '''
    Create a function that returns a tuple (a, b), where 'a' is
    the largest of negative integers, and 'b' is the smallest
    of positive integers in a list.
    If there is no negative or positive integers, return them as None.

    Examples:
    foo([2, 4, 1, 3, 5, 7]) == (None, 1)
    foo([]) == (None, None)
    foo([0]) == (None, None)
    '''
    # Your code here
    if not lst:
        return (None, None)
    neg = [x for x in lst if x < 0]
    pos = [x for x in lst if x > 0]
    if not neg:
        return (None, min(pos))
    if not pos:
        return (max(neg), None)
    return (max(neg), min(pos))
