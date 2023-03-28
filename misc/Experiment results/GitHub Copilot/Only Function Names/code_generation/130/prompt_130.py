
def tri(n):
    """Returns the nth triangular number."""
    if n == 1:
        return 1
    else:
        return n + tri(n - 1)