
from functools import reduce


def xorGame(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    #
    # 偶数 小红赢
    # 奇数 小明赢
    # b = 0
    # for i in nums:
    #     b ^= i
    # print(b, reduce(lambda x, y: x ^ y, nums+[0]))
    return reduce(lambda x, y: x ^ y, nums+[0]) != 0 and len(nums) % 2 == 0


print(xorGame([1, 1, 2]))
print(xorGame([1, 1, 1, 2]))
print(xorGame([1, 1, 2, 2]))
print(xorGame([]))
# False
# True
# False
# False 
