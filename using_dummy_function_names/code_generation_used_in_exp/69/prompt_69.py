
def foo(lst):
    '''
    You are given a non-empty list of positive integers. Return the greatest integer that is greater than 
    zero, and has a frequency greater than or equal to the value of the integer itself. 
    The frequency of an integer is the number of times it appears in the list.
    If no such a value exist, return -1.
    Examples:
        foo([4, 1, 2, 2, 3, 1]) == 2
        foo([1, 2, 2, 3, 3, 3, 4, 4, 4]) == 3
        foo([5, 5, 4, 4, 4]) == -1
    '''
    if not lst:
        return -1
    for i in range(len(lst)):
        if lst[i] > 0 and lst.count(lst[i]) >= lst[i]:
            return lst[i]
    return -1
