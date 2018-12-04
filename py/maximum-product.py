def maximumProduct(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    nums.sort()
    return max(nums[0]*nums[1]*nums[-1], nums[-1]*nums[-2]*nums[-3])


print(maximumProduct([1, 2, 3]))
print(maximumProduct([-11, -2, 3, 4, 5]))
# 6
# 110