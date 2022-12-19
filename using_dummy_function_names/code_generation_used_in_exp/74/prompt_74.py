
def foo(lst1, lst2):
    '''
    Write a function that accepts two lists of strings and returns the list that has 
    total number of chars in the all strings of the list less than the other list.

    if the two lists have the same number of chars, return the first list.

    Examples
    foo([], []) ➞ []
    foo(['hi', 'admin'], ['hI', 'Hi']) ➞ ['hI', 'Hi']
    foo(['hi', 'admin'], ['hi', 'hi', 'admin', 'project']) ➞ ['hi', 'admin']
    foo(['hi', 'admin'], ['hI', 'hi', 'hi']) ➞ ['hI', 'hi', 'hi']
    foo(['4'], ['1', '2', '3', '4', '5']) ➞ ['4']
    '''
    return sorted(lst1, key=lambda x: len(x), reverse=True) if len(lst1) > len(lst2) else sorted(lst2, key=lambda x: len(x), reverse=True)
