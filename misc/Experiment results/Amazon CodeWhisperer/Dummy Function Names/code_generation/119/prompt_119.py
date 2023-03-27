
def foo(lst):
    '''
    You are given a list of two strings, both strings consist of open
    parentheses '(' or close parentheses ')' only.
    Your job is to check if it is possible to concatenate the two strings in
    some order, that the resulting string will be good.
    A string S is considered to be good if and only if all parentheses in S
    are balanced. For example: the string '(())()' is good, while the string
    '())' is not.
    Return 'Yes' if there's a way to make a good string, and return 'No' otherwise.

    Examples:
    foo(['()(', ')']) == 'Yes'
    foo([')', ')']) == 'No'
    '''
    # Your code here
    if len(lst[0]) == 0 or len(lst[1]) == 0:
        return 'No'
    if lst[0][-1] == ')' or lst[1][0] == '(':
        return 'No'
    return 'Yes'
