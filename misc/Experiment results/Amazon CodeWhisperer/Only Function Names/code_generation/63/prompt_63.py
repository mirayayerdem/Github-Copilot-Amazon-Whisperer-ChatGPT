

def fibfib(n: int):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibfib(n-1) + fibfib(n-2)
