
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
    lst3 = []
    for i in lst1:
        if len(i) < len(lst2[0]):
            lst3.append(i)
    for i in lst2:
        if len(i) < len(lst1[0]):
            lst3.append(i)
    return lst3
