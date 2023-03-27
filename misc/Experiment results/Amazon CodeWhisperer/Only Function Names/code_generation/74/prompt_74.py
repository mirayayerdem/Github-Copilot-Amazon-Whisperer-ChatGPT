
def total_match(lst1, lst2):
    """
    lst1: list of strings
    lst2: list of strings
    """
    total = 0
    for i in range(len(lst1)):
        if lst1[i] == lst2[i]:
            total += 1
    return total


