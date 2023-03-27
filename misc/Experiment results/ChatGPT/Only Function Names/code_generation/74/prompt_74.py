
def total_match(lst1, lst2):
    count = 0
    for elem in lst1:
        if elem in lst2:
            count += 1
    return count
