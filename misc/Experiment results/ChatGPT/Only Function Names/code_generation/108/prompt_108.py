
def count_nums(arr):
    return sum(1 for x in arr if isinstance(x, (int, float)))
