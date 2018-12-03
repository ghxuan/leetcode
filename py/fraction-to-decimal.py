
def fractionToDecimal(numerator, denominator):
    """
    :type numerator: int
    :type denominator: int
    :rtype: str
    """
    n, d = divmod(numerator, denominator)
    res = f'{n}'
    decimals = []
    n, d = divmod(d * 10, denominator)
    decimals.append(n)
    while d:
        if decimals.index(n) != len(decimals)-1:
            decimals.insert(decimals.index(n), '(')
            decimals[-1] = ')'
            break
        n, d = divmod(d*10, denominator)
        decimals.append(n)
    return res+'.'+''.join([str(i) for i in decimals])


print(fractionToDecimal(1, 2))
print(fractionToDecimal(2, 1))
print(fractionToDecimal(2, 3))
print(fractionToDecimal(1, 3))
print(fractionToDecimal(1, 6))
print(fractionToDecimal(1, 7))
print(fractionToDecimal(1, 9))
print(fractionToDecimal(1, 11))
print(fractionToDecimal(1, 13))
# 0.5
# 2.0
# 0.(6)
# 0.(3)
# 0.1(6)
# 0.(142857)
# 0.(1)
# 0.(09)
# 0.(076923)
