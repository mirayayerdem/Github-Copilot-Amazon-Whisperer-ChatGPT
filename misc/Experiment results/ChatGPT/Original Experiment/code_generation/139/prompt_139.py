def special_factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
        for j in range(1, i):
            result *= j
    return result