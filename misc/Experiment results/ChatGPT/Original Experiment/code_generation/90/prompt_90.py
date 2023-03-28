def next_smallest(lst):
    if not lst:
        return None
    elif len(lst) < 2:
        return None
    else:
        return sorted(set(lst))[1]
