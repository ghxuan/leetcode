
def trailingZeroes(n):
    """
    :type n: int
    :rtype: int
    """
    # 若想要尾数为 0 ，那么必须大于 5 ，且每过一个 5 的倍数，尾数就多加一个 0 ，注意 25 和 125 这样的数不止一个 5
    # 先判断有几个 5 的倍数，再判断有几个 25 的倍数。。。
    return n // 5 + trailingZeroes(n // 5) if n else 0


for i in range(5, 131, 5):
    print(trailingZeroes(i), i)
