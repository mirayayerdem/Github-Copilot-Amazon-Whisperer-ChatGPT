def is_sorted(lst):
    for i in range(len(lst)-1):
        if lst[i] > lst[i+1]:
            return False
    if len(set(lst)) == len(lst):
        return True
    else:
        return False
