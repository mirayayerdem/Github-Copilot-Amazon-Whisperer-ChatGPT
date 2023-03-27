
def next_smallest(lst):
    '''
    lst: list of integers
    returns: list of integers
    '''
    # Your code here
    lst.sort()
    return lst[1:]
