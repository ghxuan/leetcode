
def reverse(x):
    """
    :type x: int
    :rtype: int
    """
    x = str(x).strip('0')
    if '-' in x:
        x = -int(x[:0:-1])
    else:
        x = int(x[::-1])
    if -2**31 <= x <= 2**31-1:
        return x
    return 0


print(reverse(123))
print(reverse(-123))
print(reverse(-120))
print(reverse(2**31))
# 321
# -321
# -21
# 0
