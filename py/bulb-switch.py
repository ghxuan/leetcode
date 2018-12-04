def bulb_switch(n):
    """
    :type n: int
    :rtype: int
    """
    # for i in n
    # 当 i 的质因数的数目 k 为奇数时，
    # 灯泡经过 k+2 次 置换， 灯泡是亮的
    # 假如 i 的一个因数 为 o，
    # 那么一定有相对应的因数 i/o
    # 所以 假如 i 的质因数的数目为奇数
    # 有且只有 i/o = o,
    # 即，i 为完全平方数
    # 1**2 2**2 3**2 4**2 5**2 6**2
    # int(n**0.5)**2 <= n
    # 完全平方数的数目为 int(n**0.5)
    return int(n**0.5)


print(bulb_switch(3))
# 1