
def isPowerOfTwo(n):
    """
    :type n: int
    :rtype: bool
    """
    # 假如 n 是二的 m 次幂，那么 n 只有在首位为 1 ，n - 1 全为 1，它们相与结果为 0 。
    return n > 0 and not n & (n - 1)


print(isPowerOfTwo(1))
print(isPowerOfTwo(16))
print(isPowerOfTwo(218))
# True
# True
# False
