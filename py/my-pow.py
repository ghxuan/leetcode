
def myPow(x, n):
    """
    :type x: float
    :type n: int
    :rtype: float
    """
    res = 1
    for _ in range(abs(n)):
        res *= x
    return float('%.5f' % round(res if n >= 0 else 1 / res, 5))


print(myPow(2.00000, 10))
print(myPow(2.10000, 3))
print(myPow(2.00000, -2))

# 1024.0
# 9.261
# 0.25
