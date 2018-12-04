def reachNumber(target):
    """
    :type target: int
    :rtype: int
    """
    if not target:
        return 0
    target = abs(target)
    # n^2 + n - 2*target = 0 解方程
    n = ((1 + 8 * target) ** 0.5 - 1) * 0.5
    res = int(n)
    if n.is_integer():
        return res
    res += 1
    n = sum([i for i in range(1, res + 1)])
    while 1:
        # 当 一直向一个方向走的步数之和 n 和 target 之差是 2 的倍数时，表明可以向反方向走 二分之一的之差 的步数。这时步数最小
        temp = (n - target) % 2
        if not temp:
            return res
        # 因为 n 被取整了，所以一定小于 target ，每前进一步 res 自增 1 ，n 自增 res
        res += 1
        n += res


print(reachNumber(3))
print(reachNumber(2))
# 2
# 3