
def exchange(lst1, lst2):
    """
    Exchange the contents of two lists.
    """
    lst1[:], lst2[:] = lst2[:], lst1[:]
