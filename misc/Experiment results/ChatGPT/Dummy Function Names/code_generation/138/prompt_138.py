
def foo(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    foo(4) == False
    foo(6) == False
    foo(8) == True
    """
    if n < 8:
        return False
    for a in range(2, (n//4)*2+1, 2):
        for b in range(a, (n//3)*2+1, 2):
            for c in range(b, (n//2)*2+1, 2):
                d = n - a - b - c
                if d > c and d % 2 == 0:
                    return True
    return False
