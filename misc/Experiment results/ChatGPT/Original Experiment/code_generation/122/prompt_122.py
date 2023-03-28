def add_elements(arr, k):
    return sum(x for x in arr[:k] if 0 <= x < 100)
