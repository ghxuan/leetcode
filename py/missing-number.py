
def missingNumber(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    # return [i for i in range(len(nums)+1) if i not in nums][0]
    # 让 0 代替丢失的数字
    return int(0.5*len(nums)*(len(nums)+1))-sum(nums)
    # nums.sort()
    # left = 0
    # right = len(nums)
    # while left < right:
    #     mid = int(left + (right - left) / 2)
    #     if nums[mid] > mid:
    #         right = mid
    #     else:
    #         left = mid + 1
    # return right


print(missingNumber([0, 2, 3, 4]))
print(missingNumber([0, 1, 3, 4]))
print(missingNumber([0, 1, 2, 4]))
print(missingNumber([1, 2, 3, 4, 5, 7, 0]))
# 1
# 2
# 3
# 6
