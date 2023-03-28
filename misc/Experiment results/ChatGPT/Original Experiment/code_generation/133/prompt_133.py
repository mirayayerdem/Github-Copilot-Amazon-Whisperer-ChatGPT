import math

def sum_squares(lst):
    return sum([math.ceil(x) ** 2 for x in lst])
