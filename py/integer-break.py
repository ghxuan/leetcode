def integerBreak(n):
    """
    2 1+1 1。
    3 2+1 2。
    4 2+2 4。
    5 3+2 6。
    6 3+3 9。
    7 3+4 12。
    8 3+3+2 18。
    9 3+3+3 27。
    10 3+3+4 36。
    3 的个数 3 次一轮回
    :type n: int
    :rtype: int
    """
    if n == 2 or n == 3:
        return n - 1
    if n == 4:
        return n
    n -= 5
    return 3 ** (n // 3 + 1) * (n % 3 + 2)


print(integerBreak(2))
print(integerBreak(10))
# 1
# 36