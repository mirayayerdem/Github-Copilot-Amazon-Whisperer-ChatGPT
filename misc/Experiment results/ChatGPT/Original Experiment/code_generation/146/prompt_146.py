def specialFilter(nums):
    return sum(1 for num in nums if num > 10 and str(num)[0] in "13579" and str(num)[-1] in "13579")