
def foo(a, b, c):
    '''
    Given the lengths of the three sides of a triangle. Return the area of
    the triangle rounded to 2 decimal points if the three sides form a valid triangle. 
    Otherwise return -1
    Three sides make a valid triangle when the sum of any two sides is greater 
    than the third side.
    Example:
    foo(3, 4, 5) == 6.00
    foo(1, 2, 10) == -1
    '''
    if a + b > c and a + c > b and b + c > a:
        return round((a + b + c) / 2, 2)
    return -1
