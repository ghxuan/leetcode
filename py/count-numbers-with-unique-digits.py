from functools import reduce


def countNumbersWithUniqueDigits(n):
    """
    首先， 0 也是一个数
    其次， 第一个数除非是个位数，否则不能为 0
    那么， 第一个数有 [1~9] 共 9 种可能，第二个数有 [0~9] -1 共 9 种可能，第三个数有 [0~9] -2 共 8 种可能，第四个数有 [0~9] -3 共 7 种可能 ··· ···
    最后，结果就为 9*9*8* ··· 与上一次 n-1 之和
    当 n 大于 10 时，虽然最后结果会持续相等，但为了节省计算 加一个判断 if n > 10:
    :type n: int
    :rtype: int
    """
    if not n:
        return 1
    if n > 10:
        return countNumbersWithUniqueDigits(10)
    return reduce(lambda x, y: x * y, [9 - i for i in range(n - 1)] + [9]) + countNumbersWithUniqueDigits(
        n - 1)


print(countNumbersWithUniqueDigits(1))
print(countNumbersWithUniqueDigits(2))
print(countNumbersWithUniqueDigits(3))
print(countNumbersWithUniqueDigits(9))
print(countNumbersWithUniqueDigits(10))
print(countNumbersWithUniqueDigits(11))
# 10
# 91
# 739
# 5611771
# 8877691
# 8877691