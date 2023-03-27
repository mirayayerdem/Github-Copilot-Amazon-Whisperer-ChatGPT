
def foo(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    foo([2, 3, 4, 1, 2, 4]) == 1
    foo([-1, -2, -3]) == -6
    """
    min_sum = float('inf')
    current_sum = 0
    for num in nums:
        current_sum += num
        min_sum = min(min_sum, current_sum)
        current_sum = max(current_sum, 0)
    return min_sum
