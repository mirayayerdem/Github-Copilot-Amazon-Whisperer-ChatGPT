
def strange_sort_list(lst):
    lst.sort(key=lambda x: (x % 2, x))
    return lst

