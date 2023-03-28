def f(n):
    res = []
    for i in range(1, n+1):
        if i % 2 == 0:
            res.append(factorial(i))
        else:
            res.append(sum(range(1, i+1)))
    return res

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)
