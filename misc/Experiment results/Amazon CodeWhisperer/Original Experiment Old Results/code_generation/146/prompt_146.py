
def specialFilter(nums):
    """Write a function that takes an array of numbers as input and returns 
    the number of elements in the array that are greater than 10 and both 
    first and last digits of a number are odd (1, 3, 5, 7, 9).
    For example:
    specialFilter([15, -73, 14, -15]) => 1 
    specialFilter([33, -2, -3, 45, 21, 109]) => 2
    """
    # your code here
    count = 0
    for i in nums:
        if i > 10 and i % 10 % 2 == 1 and i // 10 % 10 % 2 == 1:
            count += 1
    return count
