
def match_parens(lst):
    '''
    lst: a list of strings
    returns: True if all the strings in lst are matched by their counterparts
    '''
    # Your code here
    for i in range(len(lst)):
        if lst[i] == "(":
            if lst[i+1] == ")":
                return True
            else:
                return False
    return True

