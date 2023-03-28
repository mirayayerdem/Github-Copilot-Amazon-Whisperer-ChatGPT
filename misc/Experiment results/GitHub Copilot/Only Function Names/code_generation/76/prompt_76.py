
def is_simple_power(x, n):
    return x == n or (x % n == 0 and is_simple_power(x // n, n))