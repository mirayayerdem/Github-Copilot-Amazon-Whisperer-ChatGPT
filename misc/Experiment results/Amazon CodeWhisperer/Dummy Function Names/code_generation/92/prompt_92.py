
def foo(x, y, z):
    '''
    Create a function that takes 3 numbers.
    Returns true if one of the numbers is equal to the sum of the other two, and all numbers are integers.
    Returns false in any other cases.

    Examples
    foo(5, 2, 7) ➞ True

    foo(3, 2, 2) ➞ False

    foo(3, -2, 1) ➞ True

    foo(3.6, -2.2, 2) ➞ False



    '''
    if x == y + z or y == x + z or z == x + y:
        if type(x) == int and type(y) == int and type(z) == int:
            return True
        else:
            return False
    else:
        return False
