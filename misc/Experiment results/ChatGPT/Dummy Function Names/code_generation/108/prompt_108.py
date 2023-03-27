
def foo(arr):
    """
    Write a function count_nums which takes an array of integers and returns
    the number of elements which has a sum of digits > 0.
    If a number is negative, then its first signed digit will be negative:
    e.g. -123 has signed digits -1, 2, and 3.
    >>> foo([]) == 0
    >>> foo([-1, 11, -11]) == 1
    >>> foo([1, 1, 2]) == 3
    """
    def digit_sum(num):
        return sum([int(x) for x in str(num)])

    count = 0
    for num in arr:
        if digit_sum(num) > 0:
            count += 1
    return count
