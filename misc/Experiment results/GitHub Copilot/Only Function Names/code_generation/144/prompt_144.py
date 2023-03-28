
def simplify(x, n):
    if n == 0:
        return x
    else:
        return simplify(x + n % 10, n // 10)