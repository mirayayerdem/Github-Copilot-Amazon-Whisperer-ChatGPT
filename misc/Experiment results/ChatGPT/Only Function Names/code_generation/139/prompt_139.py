def special_factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
        for digit in str(result):
            result += int(digit)
    return result
