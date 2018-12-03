
def mirrorReflection(p, q):
    """
    :type p: int
    :type q: int
    :rtype: int
    """
    if 0 > q or p < q:
        return
    pq_gcd = gcd(p, q)
    p_amount = q // pq_gcd
    q_amount = p // pq_gcd
    print('正方形的总计和边长的乘积 : {} * {} == \n'
          '折射的总计和距离的乘积 : {} * {}'
          .format(p_amount, p, q_amount, q))
    # 当折射偶数次时：
    # 一定是射向 2 的。
    # 当折射奇数次时：
    # 正方形的数量为偶数时，射向 0；
    # 正方形的数量为奇数时，射向 1；
    return 2 if not q_amount % 2 else 1 if p_amount % 2 else 0


def gcd(a, b):
    # 用辗转相除法求两个非零整数的最大公因数
    # 辗转相除法理解： 求得 a % b 和 b 的最大公因数，a 是 n 倍的 b 和 a % b 之和
    return gcd(b, a % b) if b else a


print(mirrorReflection(2, 1))
print(mirrorReflection(3, 1))
print(mirrorReflection(3, 2))
print(mirrorReflection(4, 3))
# 正方形的总计和边长的乘积 : 1 * 2 == 
# 折射的总计和距离的乘积 : 2 * 1
# 2
# 正方形的总计和边长的乘积 : 1 * 3 == 
# 折射的总计和距离的乘积 : 3 * 1
# 1
# 正方形的总计和边长的乘积 : 2 * 3 == 
# 折射的总计和距离的乘积 : 3 * 2
# 0
# 正方形的总计和边长的乘积 : 3 * 4 == 
# 折射的总计和距离的乘积 : 4 * 3
# 2
