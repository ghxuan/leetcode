def isSelfCrossing(x):
    """
    空间复杂度(Space Complexity)是对一个算法在运行过程中临时占用存储空间大小的量度，记做S(n)=O(f(n))。
    当一个算法的空间复杂度为一个常量，即不随被处理数据量n的大小而改变时，可表示为O(1)。
    :type x: List[int]
    :rtype: bool
    """
    if not all([i > 0 for i in x]):
        return None
    length = len(x)
    if length < 4:
        return False
    eq = False
    for i in range(2, length):
        if x[i] <= x[i - 2]:
            if not eq:
                eq = True
                # 当第一次大于变成小于时，而且 4 <= i <= length - 2 ，
                # 这时如果要相遇 它的下一个的长度 和 上一次与其方向相同的长度 之和  
                # 一定要大于等于 下一个的长度
                if 3 < i < length - 1:
                    if x[i + 1] >= x[i - 1] - x[i - 3]:
                        return True
            # 只要有连续三个值相同一定会相遇，因为数组 x 有 n 个正数。
            if x[i] == x[i - 1] == x[i - 2]:
                return True
        # 当第三个数小于后，一旦小于变成大于后，一定会相遇。
        elif eq:
            return True
    return False


print(isSelfCrossing([2, 1, 1, 2]))
print(isSelfCrossing([1, 2, 3, 4]))
print(isSelfCrossing([1, 1, 1, 1]))
print(isSelfCrossing([1, 2, 3, 4, 1, 1, 1]))
print(isSelfCrossing([2, 2, 3, 4, 3, 3]))

# True
# False
# True
# True
# True