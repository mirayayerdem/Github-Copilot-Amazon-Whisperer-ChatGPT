
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
    lst.sort()
    res = []
    for i in range(len(lst)):
        if i % 2 == 0:
            res.append(lst[i])
        else:
            res.append(lst[-i-1])
    return res
