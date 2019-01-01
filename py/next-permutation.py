def next_permutation(nums):
    """
    :type nums: List[int]
    :rtype: void Do not return anything, modify nums in-place instead.
    """
    n = len(nums)
    i = n - 1
    j = n - 1
    while i:
        # 找到出现转折的地方
        if nums[i] > nums[i - 1]:
            cur = i - 1
            temp = nums[cur]
            nums[cur:] = sorted(nums[cur:])
            while j:
                # 从后向前 从已排序中找到比 temp 大一点的数
                if temp == nums[j]:
                    nums.insert(cur, nums.pop(j+1))
                    print(nums)
                    return
                j -= 1
        i -= 1
    nums.sort()
    print(nums)


next_permutation([1, 2, 3])
next_permutation([3, 2, 1])
next_permutation([1, 1, 5])
next_permutation([1, 2, 7, 4, 3, 1])
next_permutation([1, 2, 7, 4, 1, 3])
# [1, 3, 2]
# [1, 2, 3]
# [1, 5, 1]
# [1, 3, 1, 2, 4, 7]
# [1, 2, 7, 4, 3, 1]