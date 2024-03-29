
def foo(lst):
    '''
    Given a list of numbers, return whether or not they are sorted
    in ascending order. If list has more than 1 duplicate of the same
    number, return False. Assume no negative numbers and only integers.

    Examples
    foo([5]) ➞ True
    foo([1, 2, 3, 4, 5]) ➞ True
    foo([1, 3, 2, 4, 5]) ➞ False
    foo([1, 2, 3, 4, 5, 6]) ➞ True
    foo([1, 2, 3, 4, 5, 6, 7]) ➞ True
    foo([1, 3, 2, 4, 5, 6, 7]) ➞ False
    foo([1, 2, 2, 3, 3, 4]) ➞ True
    foo([1, 2, 2, 2, 3, 4]) ➞ False
    '''
    return sorted(lst) == lst and len(set(lst)) == len(lst)
