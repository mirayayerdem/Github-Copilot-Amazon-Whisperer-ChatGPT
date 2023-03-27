
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
    neg_max = None
    pos_min = None
    for i in lst:
        if i < 0:
            if neg_max is None or i > neg_max:
                neg_max = i
        elif i > 0:
            if pos_min is None or i < pos_min:
                pos_min = i
    return (neg_max, pos_min)
