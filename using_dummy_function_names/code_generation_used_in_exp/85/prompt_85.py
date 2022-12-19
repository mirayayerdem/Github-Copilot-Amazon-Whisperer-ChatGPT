
def foo(lst):
    """Given a non-empty list of integers lst. foo the even elements that are at odd indices..


    Examples:
        foo([4, 2, 6, 7]) ==> 2 
    """
    return sum(lst[i] for i in range(len(lst)) if i % 2 == 1)
