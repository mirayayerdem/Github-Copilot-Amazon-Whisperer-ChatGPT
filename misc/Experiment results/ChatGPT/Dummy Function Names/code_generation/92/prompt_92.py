
def foo(x, y, z):
    '''
    Create a function that takes 3 numbers.
    Returns true if one of the numbers is equal to the sum of the other two, and all numbers are integers.
    Returns false in any other cases.
    
    Examples
    foo(5, 2, 7) -> True
    
    foo(3, 2, 2) -> False

    foo(3, -2, 1) -> True
    
    foo(3.6, -2.2, 2) -> False
  

    
    '''
    if not all(map(lambda x: isinstance(x, int), [x, y, z])):
        return False
    return x + y == z or x + z == y or y + z == x
