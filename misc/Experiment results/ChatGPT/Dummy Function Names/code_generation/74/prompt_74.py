
def foo(lst1, lst2):
    '''
    Write a function that accepts two lists of strings and returns the list that has 
    total number of chars in the all strings of the list less than the other list.

    if the two lists have the same number of chars, return the first list.

    Examples
    foo([], []) -> []
    foo(['hi', 'admin'], ['hI', 'Hi']) -> ['hI', 'Hi']
    foo(['hi', 'admin'], ['hi', 'hi', 'admin', 'project']) -> ['hi', 'admin']
    foo(['hi', 'admin'], ['hI', 'hi', 'hi']) -> ['hI', 'hi', 'hi']
    foo(['4'], ['1', '2', '3', '4', '5']) -> ['4']
    '''
    lst1_chars = sum([len(x) for x in lst1])
    lst2_chars = sum([len(x) for x in lst2])
    if lst1_chars < lst2_chars:
        return lst1
    elif lst1_chars > lst2_chars:
        return lst2
    else:
        return lst1

