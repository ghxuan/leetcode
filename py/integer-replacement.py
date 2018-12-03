
def integerReplacement(n):
    """
    :type n: int
    :rtype: int
    """
    if n == 1:
        return 0
    if n % 2:
        # 加 1 除 2 为 2 步
        return 2 + min(integerReplacement((n + 1) // 2), integerReplacement((n - 1) // 2))
    # 除 2 为 1 步
    return 1 + integerReplacement(n // 2)


print(integerReplacement(31))
print(integerReplacement(384))
print(integerReplacement(15))
print(integerReplacement(9))
print(integerReplacement(8))
print(integerReplacement(7))
# 6
# 9
# 5
# 4
# 3
# 4
