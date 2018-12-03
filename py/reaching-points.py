
def reachingPoints(sx, sy, tx, ty):
    """
    :type sx: int
    :type sy: int
    :type tx: int
    :type ty: int
    :rtype: bool
    """
    # 当出现等于或小于时立刻跳出
    while tx > sx and ty > sy:
        if tx > ty:
            # 最开始是使用减等，但是对于那种成倍数的太慢了
            tx %= ty
        else:
            ty %= tx
    if tx < sx or ty < sy:
        return False
    # 当出现相等的时候，另一个数的 t 与 s 之差是相等的数的 n 倍时，才会返回 True
    return (tx == sx and not (ty - sy) % sx) or (ty == sy and not (tx - sx) % sy)


print(reachingPoints(1, 1, 3, 5))
print(reachingPoints(1, 2, 1, 10 ** 9))
# True
# True
