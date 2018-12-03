


def superPow(a, b):
    """
    :type a: int
    :type b: List[int]
    :rtype: int
    """
    b.reverse()
    super_pow = 1
    for i in range(len(b)):
        super_pow *= Pow(Pow(a, b[i]), Pow(10, i))
    return super_pow % 1337


def Pow(a, b):
    """
    :param a: int
    :param b: int
    :return: int
    """
    res = 1
    while b:
        if b % 2:
            res *= a
        a *= a
        b >>= 1
    return res


print(superPow(2, [3]))
print(superPow(2, [1, 0]))
print(superPow(2, [1, 0, 0, 0, 0, 0, 0]))


# 8
# 1024
# 562

