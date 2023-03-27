import math
def foo(x, n):
    """Your task is to write a function that returns true if a number x is a simple
    power of n and false in other cases.
    x is a simple power of n if n**int=x
    For example:
    foo(1, 4) => true
    foo(2, 2) => true
    foo(8, 2) => true
    foo(3, 2) => false
    foo(3, 1) => false
    foo(5, 3) => false
    """
    if n==1:
        return False
    elif x == 1:
        return True
    elif x == n:
        return True
    elif x < n:
        return False
    else:
        return x == n ** int(math.log(x,n))
