def minSubArraySum(nums):
    min_sum = float("inf")
    current_sum = 0
    for num in nums:
        current_sum = min(current_sum + num, num)
        min_sum = min(min_sum, current_sum)
    return min_sum
