
def exchange(lst1, lst2):
    lst1.extend(lst2)
    lst2.clear()
    return lst1, lst2
