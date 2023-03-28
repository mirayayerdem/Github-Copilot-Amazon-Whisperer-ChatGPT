
def special_factorial(n):
    if n == 0:
        return 1
    else:
        return n * special_factorial(n - 1)
        