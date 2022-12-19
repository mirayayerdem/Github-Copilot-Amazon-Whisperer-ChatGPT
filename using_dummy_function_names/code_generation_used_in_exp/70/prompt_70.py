
def foo(lst):
    '''
    Given list of integers, return list in strange order.
    Strange sorting, is when you start with the minimum value,
    then maximum of the remaining integers, then minimum and so on.

    Examples:
    foo([1, 2, 3, 4]) == [1, 4, 2, 3]
    foo([5, 5, 5, 5]) == [5, 5, 5, 5]
    foo([]) == []
    '''
    return sorted(lst, reverse=True)
