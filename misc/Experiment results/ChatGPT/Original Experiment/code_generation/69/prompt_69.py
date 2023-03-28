def search(lst):
    counts = {}
    for x in lst:
        if x in counts:
            counts[x] += 1
        else:
            counts[x] = 1
    result = -1
    for x in sorted(counts, reverse=True):
        if x <= counts[x]:
            result = x
    return result
