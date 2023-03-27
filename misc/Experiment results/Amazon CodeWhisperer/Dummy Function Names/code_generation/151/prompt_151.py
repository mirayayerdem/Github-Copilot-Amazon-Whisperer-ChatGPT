
def foo(lst):
    '''
    Given a list of numbers, return the sum of squares of the numbers
    in the list that are odd. Ignore numbers that are negative or not integers.

    foo([1, 3, 2, 0]) == 1 + 9 + 0 + 0 = 10
    foo([-1, -2, 0]) == 0
    foo([9, -2]) == 81
    foo([0]) == 0  

    If the input list is empty, return 0.
    '''
    # Your code here
    sum = 0
    for i in lst:
        if i > 0 and i % 2 != 0:
            sum += i ** 2
    return sum
