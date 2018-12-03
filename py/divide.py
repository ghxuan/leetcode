
def divide(dividend, divisor):
    """
    :type dividend: int
    :type divisor: int
    :rtype: int
    """
    if not divisor or (divisor == 1 and dividend == -2147483648):
        return 2147483647
    end, sor = abs(dividend), abs(divisor)
    res = 0
    while end > sor:
        end -= sor
        res += 1
    return res if plus_or_minus(dividend) == plus_or_minus(divisor) else -res


def plus_or_minus(x):
    if abs(x) == x:
        return True
    return False


print(divide(10, 3))
print(divide(7, -3))
print(divide(10, 0))
print(divide(-2147483648, 1))
# 3
# -2
# 2147483647
# 2147483647
