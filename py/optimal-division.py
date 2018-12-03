
def optimalDivision(nums):
    """
    :type nums: List[int]
    :rtype: str
    """
    # 若实现最大，则第二个数后面的所有的数搜要乘起来。
    length = len(nums)
    if not length:
        return ''
    elif length == 1:
        return str(nums[0])
    elif length == 2:
        return '/'.join([str(i) for i in nums])
    return str(nums[0]) + '/(' + '/'.join([str(i) for i in nums[1:]]) + ')'


print(optimalDivision([1, 2, 3, 4]))
print(optimalDivision([1000, 100, 10, 2]))
# 1/(2/3/4)
# 1000/(100/10/2)
