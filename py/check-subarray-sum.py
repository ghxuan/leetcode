
def checkSubarraySum(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: bool
    """
    res = []
    sum_ = last = nums[0]
    # 首先，需要了解 a%k = c, b%k=c,
    # 那么，a-b = m*k
    # 假如，前 i 项和 sum(i)%k=c ，
    # 前 j 项和 sum(j)%k=c
    # sum(j-i) 为 k 的倍数，
    # 返回 True
    # 返回 True
    for j in nums[1:]:
        sum_ += j
        temp = sum_ % k if k else sum_
        if temp in res:
            return True
        else:
            # 添加上一个的 temp
            res.append(last)
            last = temp
    return False


print(checkSubarraySum([23, 0, 0, 6, 7], 0))
print(checkSubarraySum([23, 4, 0, 5, 7], 0))
print(checkSubarraySum([23, 4, 0, 5, 0, 0], 0))
print(checkSubarraySum([23, 2, 4, 6, 7], 6))
print(checkSubarraySum([23, 2, 6, 4, 7], 6))
print(checkSubarraySum([1, 2, 3, 4, 5], 17))
print(checkSubarraySum([i for i in range(10000)], 5 * 10 ** 7))
# True
# False
# True
# True
# True
# False
# False
