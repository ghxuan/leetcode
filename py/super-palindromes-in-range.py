


def superPalindromesInRange(L, R):
    """
    :type L: str
    :type R: str
    :rtype: int
    """
    res = 0
    for i in range(int(L), int(R)):
        if isPalindromes(str(i)) and isPalindromes(str(i ** 0.5)[:-2]):
            res += 1
            print(i)
    print()
    return res


def isPalindromes(a):
    """
    :param a: str
    :return: bool
    """
    return a == a[::-1]


print(superPalindromesInRange('4', '1000'))
print()
print(superPalindromesInRange('0', '100000000'))

# 4
# 9
# 121
# 484

# 4

# 0
# 1
# 4
# 9
# 121
# 484
# 10201
# 12321
# 14641
# 40804
# 44944
# 1002001
# 1234321
# 4008004

# 14

