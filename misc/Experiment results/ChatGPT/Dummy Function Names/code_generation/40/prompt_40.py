

def foo(l: list):
    """
    triples_sum_to_zero takes a list of integers as an input.
    it returns True if there are three distinct elements in the list that
    sum to zero, and False otherwise.

    >>> foo([1, 3, 5, 0])
    False
    >>> foo([1, 3, -2, 1])
    True
    >>> foo([1, 2, 3, 7])
    False
    >>> foo([2, 4, -5, 3, 9, 7])
    True
    >>> foo([1])
    False
    """
    l = list(set(l))
    if len(l) < 3:
        return False
    l.sort()
    for i in range(len(l)-2):
        j = i+1
        k = len(l)-1
        while j < k:
            if l[i] + l[j] + l[k] == 0:
                return True
            elif l[i] + l[j] + l[k] < 0:
                j += 1
            else:
                k -= 1
    return False
