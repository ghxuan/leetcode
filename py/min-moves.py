def minMoves(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    # 举个例子，看看，直觉，但不知道为什么
    # 错了
    # print(len(nums)*max(nums)-sum(nums))
    # 给 n - 1 个数字加 1 ，效果等同于给那个未被选中的数字减 1
    # 每次给那个未被选中的数字减 1，直到其与最小的数相等，最小的数不变
    return sum(nums)-len(nums)*min(nums)


print(minMoves([1, 2, 3]))
print(minMoves([1, 3, 5, 7]))
print(minMoves([1, 2, 3, 4, 5]))
print(minMoves([2, 5, 6]))
# 3
# 12
# 10
# 7