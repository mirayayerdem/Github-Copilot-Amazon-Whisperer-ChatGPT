
def minSubArraySum(nums):
    min_sum = float('inf')
    current_sum = 0
    for i in range(len(nums)):
        current_sum = nums[i]
        for j in range(i+1, len(nums)):
            current_sum += nums[j]
            if current_sum < min_sum:
                min_sum = current_sum
    return min_sum
