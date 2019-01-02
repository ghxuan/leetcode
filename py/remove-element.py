def remove_element(nums, val):
    """
    :type nums: List[int]
    :type val: int
    :rtype: int
    """
    res = 0
    for index, num in enumerate(nums):
        if num != val:
            nums[res] = nums[index]
            res += 1
    return res


print(remove_element([3, 2, 2, 3], 3))
print(remove_element([0, 1, 2, 2, 3, 0, 4, 2], 2))
# 2
# 5