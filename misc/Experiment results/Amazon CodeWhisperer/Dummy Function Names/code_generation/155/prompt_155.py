
def foo(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        foo(-12) ==> (1, 1)
        foo(123) ==> (1, 2)
    """
    even = 0
    odd = 0
    for i in str(num):
        if int(i) % 2 == 0:
            even += 1
        else:
            odd += 1
    return (even, odd)
