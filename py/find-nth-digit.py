def findNthDigit(n):
    """
    :type n: int
    :rtype: int
    """
    num = 1
    length = 9
    while n > num * length:
        n -= num * length
        num += 1
        length *= 10
    # n - 1 代表数的索引从 0 开始
    temp = divmod(n - 1, num)
    return int(str(10 ** (num - 1) + temp[0])[temp[1]])


print(findNthDigit(3))
print(findNthDigit(9))
print(findNthDigit(10))
print(findNthDigit(11))
print(findNthDigit(12))
print(findNthDigit(13))
# 3
# 9
# 1
# 0
# 1
# 1