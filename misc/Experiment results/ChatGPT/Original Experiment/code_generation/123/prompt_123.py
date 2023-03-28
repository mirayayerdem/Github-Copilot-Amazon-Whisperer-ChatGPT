def get_odd_collatz(n):
    res = []
    while n != 1:
        if n % 2 != 0:
            res.append(n)
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3*n + 1
    res.append(1)
    res.sort()
    return res
