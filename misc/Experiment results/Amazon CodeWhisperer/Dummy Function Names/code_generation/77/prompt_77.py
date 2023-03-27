
def foo(a):
    '''
    Write a function that takes an integer a and returns True 
    if this ingeger is a cube of some integer number.
    Note: you may assume the input is always valid.
    Examples:
    foo(1) ==> True
    foo(2) ==> False
    foo(-1) ==> True
    foo(64) ==> True
    foo(0) ==> True
    foo(180) ==> False
    '''
    if a == 0:
        return True
    for i in range(1, a + 1):
        if i ** 3 == a:
            return True
    return False
