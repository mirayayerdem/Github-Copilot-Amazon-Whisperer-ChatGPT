
def foo(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    foo([2, 3, 4, 1, 2, 4]) == 1
    foo([-1, -2, -3]) == -6
    """
    if not nums:
        return 0
    min_sum = nums[0]
    current_sum = nums[0]
    for num in nums[1:]:
        current_sum = max(num, current_sum + num)
        min_sum = min(min_sum, current_sum)
    return min_sum
