
def foo(a, b, c):
    '''
    Given the lengths of the three sides of a triangle. Return True if the three
    sides form a right-angled triangle, False otherwise.
    A right-angled triangle is a triangle in which one angle is right angle or 
    90 degree.
    Example:
    foo(3, 4, 5) == True
    foo(1, 2, 3) == False
    '''
    sides = [a, b, c]
    sides.sort()
    return (sides[0]**2 + sides[1]**2) == sides[2]**2
