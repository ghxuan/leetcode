def next_permutation(nums):
    """
    :type nums: List[int]
    :rtype: None Do not return anything, modify nums in-place instead.
    """
    j = len(nums) - 1
    i = j - 1
    last, n_last = nums[j], nums[i]
    while i != -1 and n_last >= last:
        i -= 1
        last, n_last = n_last, nums[i]
    if i != -1:
        last = nums[j]
        while last <= n_last:
            j -= 1
            last = nums[j]
        nums[i], nums[j] = last, n_last
    nums[i + 1:] = sorted(nums[i + 1:])
    # n = len(nums)
    # j = n - 1
    # i = j - 1
    # nums_s = dict(zip(range(n), nums))
    # last, n_last = nums_s.get(j), nums_s.get(i)
    # while i != -1 and n_last >= last:
    #     i -= 1
    #     last, n_last = n_last, nums_s.get(i, 0)
    # if i != -1:
    #     last = nums_s.get(j)
    #     while last <= n_last:
    #         j -= 1
    #         last = nums_s.get(j)
    #     nums[i], nums[j] = last, n_last
    # nums[i + 1:] = sorted(nums[i + 1:])
    print(nums)


next_permutation([1, 2, 3])
next_permutation([3, 2, 1])
next_permutation([1, 1, 5])
next_permutation([1, 3, 2])
next_permutation([2, 3, 1])
next_permutation([1, 2])

# [1, 3, 2]
# [1, 2, 3]
# [1, 5, 1]
# [2, 1, 3]
# [3, 1, 2]
# [2, 1]