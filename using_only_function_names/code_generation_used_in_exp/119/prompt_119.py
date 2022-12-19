
def match_parens(lst):
    """
    Returns the number of matching parentheses in the list.
    """
    return sum(1 for num in lst if num == '(') - sum(1 for num in lst if num == ')')

