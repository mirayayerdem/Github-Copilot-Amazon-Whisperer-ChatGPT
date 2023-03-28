def strange_sort_list(lst):
    if not lst:
        return []
    sorted_lst = sorted(lst)
    result = []
    i, j = 0, len(sorted_lst) - 1
    while i <= j:
        result.append(sorted_lst[i])
        i += 1
        if i <= j:
            result.append(sorted_lst[j])
            j -= 1
    return result
