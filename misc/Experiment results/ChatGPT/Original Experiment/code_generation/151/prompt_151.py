def double_the_difference(lst):
    return sum(n**2 for n in lst if isinstance(n, int) and n > 0 and n % 2 != 0)