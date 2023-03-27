
def foo(lst):
    """Given a non-empty list of integers, return the sum of all of the odd elements that are in even positions.
    

    Examples
    foo([5, 8, 7, 1]) ==> 12
    foo([3, 3, 3, 3, 3]) ==> 9
    foo([30, 13, 24, 321]) ==>0
    """
    return sum([x for i, x in enumerate(lst) if i % 2 == 1 and x % 2 == 1])
