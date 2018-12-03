
def minMoves2(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    # 四舍五入
    res = round(sum(nums) / len(nums))
    return sum([abs(i - res) for i in nums])


print(minMoves2([1, 2, 3]))
print(minMoves2([1, 3, 5, 7]))
print(minMoves2([1, 2, 3, 4, 5]))
print(minMoves2([2, 5, 6]))
# 2
# 8
# 6
# 5
