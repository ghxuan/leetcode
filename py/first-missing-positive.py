def first_missing_positive(nums):
    """
    结果只会存在于[1,n+1],那么将1放到nums[0],2放到nums[1] ···
    :type nums: List[int]
    :rtype: int
    """
    n = len(nums)
    if n == 1:
        if nums[0] != 1:
            return 1
        else:
            return 2
    for i in range(n):
        while 0 < nums[i] <= n and nums[nums[i] - 1] != nums[i]:
            nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
    for i in range(n):
        if i + 1 != nums[i]:
            return i + 1
    return n + 1


print(first_missing_positive([2, 1, 3]))
print(first_missing_positive([1, 2, 0]))
print(first_missing_positive([3, 4, -1, 1]))
print(first_missing_positive([7, 8, 9, 11, 12]))
# [1, 2, 3]            4
# [1, 2, 0]            3
# [1, -1, 3, 4]        2
# [7, 8, 9, 11, 12]    1