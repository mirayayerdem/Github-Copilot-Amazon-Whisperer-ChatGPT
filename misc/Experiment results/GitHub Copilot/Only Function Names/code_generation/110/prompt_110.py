
def exchange(lst1, lst2):
    """Exchange the elements of lst1 and lst2."""
    for i in range(len(lst1)):
        lst1[i], lst2[i] = lst2[i], lst1[i]