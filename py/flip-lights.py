
def flip_fights(n, m):
    """
    :type n: int
    :type m: int
    :rtype: int
    """
    # 因为 [1, 2, 3···, n]
    # 所以 n >= 1
    # 大神写的，不知为何
    # return min(1 << min(n, 3), 1 + m * min(n, 3))
    if not m:
        return 1
    elif n == 1:
        return 2
    elif n == 2:
        # 00 10 01 或 00 11 01 10
        return 4 if m > 1 else 3
    else:
        # 000 101 010 100
        # 111 000 010 101 100 001 110
        # 111 000 010 101 100 001 110 011
        return 4 if m == 1 else 7 if m == 2 else 8


print(flip_fights(1, 1))
print(flip_fights(2, 1))
print(flip_fights(3, 1))
# 2
# 3
# 4
