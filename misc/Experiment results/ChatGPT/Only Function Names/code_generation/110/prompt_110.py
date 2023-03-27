
def exchange(lst1, lst2):
    lst1[:], lst2[:] = lst2[:], lst1[:]
    return lst1, lst2
