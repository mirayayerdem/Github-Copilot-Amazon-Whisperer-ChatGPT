

def fib4(n: int):
    if n < 2:
        return n
    return fib4(n-2) + fib4(n-1)
