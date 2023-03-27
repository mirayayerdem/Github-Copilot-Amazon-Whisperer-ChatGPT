
def foo(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    foo([2, 3, 4, 1, 2, 4]) == 1
    foo([-1, -2, -3]) == -6
    """
    return min([sum(nums[i:j]) for i in range(len(nums)) for j in range(i+1, len(nums)+1)])
