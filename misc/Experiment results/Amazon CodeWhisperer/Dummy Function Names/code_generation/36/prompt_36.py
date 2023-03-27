

def foo(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.
    >>> foo(50)
    0
    >>> foo(78)
    2
    >>> foo(79)
    3
    """
    count = 0
    for i in range(n):
        if i % 11 == 0 or i % 13 == 0:
            if str(i).count('7') > 0:
                count += 1
    return count
