
def numSquares(n):
    """
    :type n: int
    :rtype: int
    """
    n, temp = divmod(n, int(n ** 0.5) ** 2)
    if temp:
        n += numSquares(temp)
    return n


print(numSquares(12))
print(numSquares(13))
# 4
# 2
