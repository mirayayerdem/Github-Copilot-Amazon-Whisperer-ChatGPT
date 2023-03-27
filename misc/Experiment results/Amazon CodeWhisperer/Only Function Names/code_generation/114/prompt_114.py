
def minSubArraySum(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    min_sum = nums[0]
    sum = 0
    for i in range(len(nums)):
        sum += nums[i]
        min_sum = min(min_sum, sum)
        sum = max(sum, 0)
    return min_sum
