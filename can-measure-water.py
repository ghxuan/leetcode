

def canMeasureWater(x, y, z):
    """
    :type x: int
    :type y: int
    :type z: int
    :rtype: bool
    """
    if z > x + y:
        return False
    if z == y or z == x or z == x + y:
        return True
    return z % gcd(x, y) == 0


def gcd(x, y):
    """
    :type x: int
    :type y: int
    :rtype: int
    """
    if x < y:
        x, y = y, x
    # 递归使用辗转相除法求最大公因数
    if y == 0:
        return x
    return gcd(y, x % y)
    # 非递归使用辗转相除法求最大公因数
    # while y:
    #     x, y = y, x % y
    # return x


print(canMeasureWater(85, 34, 17))
print(canMeasureWater(3, 5, 4))
print(canMeasureWater(2, 6, 5))

