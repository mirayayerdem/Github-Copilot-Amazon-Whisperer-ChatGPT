

def sort_even(l: list):
    even = sorted([i for i in l if i % 2 == 0])
    odd = [i for i in l if i % 2 != 0]
    return even + odd
