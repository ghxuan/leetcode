def titleToNumber(s):
    """
    :type s: str
    :rtype: int
    """
    return sum([(ord(j)-64)*(26**i) for i, j in enumerate(s[::-1])])


print(titleToNumber('A'))
print(titleToNumber('AB'))
print(titleToNumber('ZY'))
# 1
# 28
# 701