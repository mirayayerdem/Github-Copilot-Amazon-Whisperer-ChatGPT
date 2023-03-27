
def foo(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    foo(30) == True
    30 = 2 * 3 * 5
    """
    if a < 100:
        for i in range(2, a):
            if a % i == 0:
                return False
        return True
    else:
        return False
