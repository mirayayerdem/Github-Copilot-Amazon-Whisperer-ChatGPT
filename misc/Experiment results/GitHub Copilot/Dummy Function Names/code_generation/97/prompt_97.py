
def foo(a, b):
    """Complete the function that takes two integers and returns 
    the product of their unit digits.
    Assume the input is always valid.
    Examples:
    foo(148, 412) should return 16.
    foo(19, 28) should return 72.
    foo(2020, 1851) should return 0.
    foo(14,-15) should return 20.
    """
    if a < 0:
        a = a * -1
    if b < 0:
        b = b * -1
    return (a % 10) * (b % 10)
