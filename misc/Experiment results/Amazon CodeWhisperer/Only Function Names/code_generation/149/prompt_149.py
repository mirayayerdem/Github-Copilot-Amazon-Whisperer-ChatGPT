
def sorted_list_sum(lst):
    if len(lst) == 1:
        return lst[0]
    else:
        return lst[0] + sorted_list_sum(lst[1:])
