

def sum_to_n(n: int):
    return [(i, n-i) for i in range(1, int(n/2)+1) if (n-i) > i]
