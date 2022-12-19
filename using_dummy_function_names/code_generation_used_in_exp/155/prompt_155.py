
def foo(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        foo(-12) ==> (1, 1)
        foo(123) ==> (1, 2)
    """
    return (sum(1 for x in str(num) if x % 2 == 0), sum(1 for x in str(num) if x % 2 == 1))
