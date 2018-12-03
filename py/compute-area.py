
def computeArea(A, B, C, D, E, F, G, H):
    """
    :type A: int
    :type B: int
    :type C: int
    :type D: int
    :type E: int
    :type F: int
    :type G: int
    :type H: int
    :rtype: int
    """
    # 求一个长方形的面积
    def s(a, b, c, d):
        return (d-b)*(c-a)

    # 面积之和减去重叠的面积。对于重叠的时候，无论几个角如何移动，左下角一定最大，右上角一定最小
    return s(A, B, C, D) + s(E, F, G, H) - s(max(A, E), max(B, F), min(C, G), min(D, H))


print(computeArea(-3, 0, 3, 4, 0, -1, 9, 2))
# 45
