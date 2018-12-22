def reverse(x):
    """
    :type x: int
    :rtype: int
    """
    if x < 0:
        x = -int(str(x)[-1:0:-1])
    else:
        x = int(str(x)[::-1])
    if -2147483648 <= x <= 2147483647:
        return x
    return 0


print(reverse(123))
print(reverse(-123))
print(reverse(-120))
print(reverse(2 ** 31))
# 321
# -321
# -21
# 0