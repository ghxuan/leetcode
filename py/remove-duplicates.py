def remove_duplicates(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    res = 0
    for i in nums:
        if i != nums[res]:
            res += 1
            nums[res] = i
    return res + 1


print(remove_duplicates([1, 1, 2]))
print(remove_duplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))
# 2
# 5