def isIdealPermutation(A):
    """
    :type A: List[int]
    :rtype: bool
    """
    # 当数组 A 中全局倒置的数量等于局部倒置的数量时，有且仅有几个相邻的两个数发生了交换
    # A 是 [0, 1, ..., A.length - 1] 的一种排列，若排好序后，索引与值相同
    # 若全局倒置的数量等于局部倒置的数量，相邻两个数与其索引只差为 0 或 +-1 
    return False if [i for n, i in enumerate(A) if abs(i - n) > 1] else True


print(isIdealPermutation([1, 0, 2]))
print(isIdealPermutation([1, 2, 0]))
print(isIdealPermutation([1, 0, 3, 2]))
# True
# False
# True