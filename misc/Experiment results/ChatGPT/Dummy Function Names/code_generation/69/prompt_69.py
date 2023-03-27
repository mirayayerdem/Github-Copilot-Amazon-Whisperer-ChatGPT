from collections import Counter
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
    c = Counter(lst)
    max_freq = max(c.values())
    max_val = -1
    for key, value in c.items():
        if value >= key and key > max_val and key <= max_freq:
            max_val = key
    return max_val

