def two_sum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    res_hash = {}
    for index, num in enumerate(nums):
        if num not in res_hash:
            res_hash[target-num] = index
        else:
            return [index, res_hash[num]]



print(two_sum([2, 7, 11, 15], 9))
# [0, 1]
# [1, 0]
# [1, 0]