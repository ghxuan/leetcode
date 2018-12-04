def isPalindrome(x):
    """
    :type x: int
    :rtype: bool
    """
    if x < 0 or not x % 10:
        return False
    res = []
    while x:
        x, i = divmod(x, 10)
        res.append(i)
    return not [i for i in range(len(res)//2+1) if res[i] != res[-1-i]]


print(isPalindrome(121))
print(isPalindrome(1221))
print(isPalindrome(-121))
print(isPalindrome(10))
# True
# True
# False
# False