def divide(dividend, divisor):
    """
    :type dividend: int
    :type divisor: int
    :rtype: int
    """
    int_max, int_min = 2147483647, -2147483648
    sign, res = 0, 0
    if 0 in [dividend, divisor]:
        return 0
    elif dividend < 0 < divisor or divisor < 0 < dividend:
        sign = -1
    dividend, divisor = abs(dividend), abs(divisor)
    while dividend >= divisor:
        tmp, val = divisor, 1
        while dividend >= tmp:
            res += val
            dividend -= tmp
            tmp += tmp
            val += val
    if sign:
        return max(int_min, -res)
    else:
        return min(int_max, res)


print(divide(10, 3))
print(divide(7, -3))
print(divide(10, 0))
print(divide(-2147483648, 1))
# 3
# -2
# 2147483647
# 2147483647