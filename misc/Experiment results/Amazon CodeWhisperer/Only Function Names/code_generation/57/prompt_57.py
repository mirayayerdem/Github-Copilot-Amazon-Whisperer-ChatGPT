

def monotonic(l: list):
    return l == sorted(l) or l == sorted(l, reverse=True)