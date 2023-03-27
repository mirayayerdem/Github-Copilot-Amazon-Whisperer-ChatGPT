
def order_by_points(nums):
    '''
    nums: list of integers
    return: list of integers
    '''
    # write your solution here
    return sorted(nums, key = lambda x: (x % 10, x // 10))

