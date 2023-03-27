
def largest_smallest_integers(lst):
    '''
    This function returns the largest and smallest integers in a list
    '''
    largest = lst[0]
    smallest = lst[0]
    for i in range(len(lst)):
        if lst[i] > largest:
            largest = lst[i]
        if lst[i] < smallest:
            smallest = lst[i]
    return largest, smallest

