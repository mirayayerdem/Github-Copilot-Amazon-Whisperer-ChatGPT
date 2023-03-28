def add(lst):
    return sum(x for i, x in enumerate(lst) if i % 2 == 1 and x % 2 == 0)
