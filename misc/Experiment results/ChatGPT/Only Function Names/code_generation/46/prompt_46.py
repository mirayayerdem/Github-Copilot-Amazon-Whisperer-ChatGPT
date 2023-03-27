

def fib4(n: int):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib4(n-1) + fib4(n-2)
