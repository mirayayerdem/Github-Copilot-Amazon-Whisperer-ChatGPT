def fib4(n: int):
    if n <= 3:  # Return 0 for n <= 3
        return 0
    elif n == 4:  # Return 2 for n = 4
        return 2
    else:  # Compute fib4(n) for n > 4
        # Initialize variables to compute fib4(n)
        a, b, c, d = 0, 0, 2, 0
        for i in range(5, n + 1):  # Iterate from i = 5 to n
            e = a + b + c + d  # Compute fib4(i)
            a, b, c, d = b, c, d, e  # Update variables
        return e
