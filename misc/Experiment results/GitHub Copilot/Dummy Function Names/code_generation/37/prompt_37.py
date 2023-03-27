

def foo(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.
    >>> foo([1, 2, 3])
    [1, 2, 3]
    >>> foo([5, 6, 3, 4])
    [3, 6, 5, 4]
    """
    l2 = []
    for i in range(len(l)):
        if i % 2 == 0:
            l2.append(sorted(l[i]))
        else:
            l2.append(l[i])
    return l2
