def primePalindrome(N):
    """
    :type N: int
    :rtype: int
    """
    while 1:
        if str(N) == str(N)[::-1]:
            temp = 0
            for i in range(2, int(N ** 0.5) + 1):
                if N % i == 0:
                    temp = 1
                    break
            if not temp:
                return N
        N += 1


print(primePalindrome(6))
print(primePalindrome(8))
print(primePalindrome(13))
print(primePalindrome(10**5))
# 7
# 11
# 101
# 1003001