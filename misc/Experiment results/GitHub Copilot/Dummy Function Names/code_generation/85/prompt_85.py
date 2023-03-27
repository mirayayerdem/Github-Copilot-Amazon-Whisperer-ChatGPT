
def foo(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        foo([4, 2, 6, 7]) ==> 2 
    """
    return sum([x for i, x in enumerate(lst) if i % 2 == 1 and x % 2 == 0])
