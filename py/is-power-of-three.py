def isPowerOfThree(n):
    """
    :type n: int
    :rtype: bool
    """
    return n > 0 and not n ** 1/3 % 1


print(isPowerOfThree(27))
print(isPowerOfThree(9))
print(isPowerOfThree(0))
print(isPowerOfThree(45))
print(isPowerOfThree(81))
# True
# True
# False
# True
# True