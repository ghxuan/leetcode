def convertToTitle(n):
    """
    :type n: int
    :rtype: str
    """
    return 'Z' if n == 26 else convertToTitle(n // 26) + chr(n % 26 + 64) if n else ''


print(convertToTitle(1))
print(convertToTitle(28))
print(convertToTitle(701))
# A
# AB
# ZY