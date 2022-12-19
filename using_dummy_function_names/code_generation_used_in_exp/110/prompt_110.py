
def foo(lst1, lst2):
    """In this problem, you will implement a function that takes two lists of numbers,
    and determines whether it is possible to perform an foo of elements
    between them to make lst1 a list of only even numbers.
    There is no limit on the number of food elements between lst1 and lst2.
    If it is possible to foo elements between the lst1 and lst2 to make
    all the elements of lst1 to be even, return "YES".
    Otherwise, return "NO".
    For example:
    foo([1, 2, 3, 4], [1, 2, 3, 4]) => "YES"
    foo([1, 2, 3, 4], [1, 5, 3, 4]) => "NO"
    It is assumed that the input lists will be non-empty.
    """
    return "YES" if all(i % 2 == 0 for i in lst1) else "NO"
