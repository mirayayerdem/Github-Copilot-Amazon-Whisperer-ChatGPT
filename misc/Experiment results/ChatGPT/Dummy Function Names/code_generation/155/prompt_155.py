
def foo(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        foo(-12) ==> (1, 1)
        foo(123) ==> (1, 2)
    """
    num = str(abs(num)) # convert the input number to string and take the absolute value to ignore negative sign
    even = sum(1 for x in num if int(x) % 2 == 0)
    odd = sum(1 for x in num if int(x) % 2 != 0)
    return (even, odd)
