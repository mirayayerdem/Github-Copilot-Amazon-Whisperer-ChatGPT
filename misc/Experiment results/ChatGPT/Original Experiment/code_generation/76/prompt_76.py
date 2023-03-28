def is_simple_power(x, n):
    i = 1
    while n ** i < x:
        i += 1
    return n ** i == x
