
def foo(nums):
    """Write a function that takes an array of numbers as input and returns 
    the number of elements in the array that are greater than 10 and both 
    first and last digits of a number are odd (1, 3, 5, 7, 9).
    For example:
    foo([15, -73, 14, -15]) => 1 
    foo([33, -2, -3, 45, 21, 109]) => 2
    """
    count = 0
    for num in nums:
        if num > 10 and num % 10 == 1 and num % 2 != 0:
            count += 1
    return count
