
def strange_sort_list(lst):
    return sorted(lst, key=lambda x: (x % 2, x))
