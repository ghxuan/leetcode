def two_sum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    # for i in nums:
    #     # in 是 python 中比较方便的方法
    #     if target-i in nums:
    #         return [nums.index(i), nums.index(target-i)]
    for i, j in enumerate(nums):
        if nums[:i].count(target-j):
            return [i, nums.index(target-j)]


print(two_sum([2, 7, 11, 15], 9))
# [0, 1]
# [1, 0]