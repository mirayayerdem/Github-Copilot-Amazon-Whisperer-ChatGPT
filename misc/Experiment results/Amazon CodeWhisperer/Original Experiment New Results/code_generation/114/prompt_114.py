
def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    # initialize the sum of the subarray
    # and the minimum sum
    sub_sum = 0
    min_sum = float('inf')
    # start with the first element
    for num in nums:
        # if the current subarray sum is less than 0
        # then we don't need it anymore
        if sub_sum < 0:
            # reset the subarray sum
            sub_sum = 0
        # add the current element to the subarray sum
        sub_sum += num
        # update the minimum sum
        min_sum = min(min_sum, sub_sum)
    # return the minimum sum
    return min_sum