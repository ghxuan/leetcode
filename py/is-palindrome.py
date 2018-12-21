def is_palindrome(x):
    """
    :type x: int
    :rtype: bool
    """
    # if x < 0 or not x % 10:
    #     return False if x else True
    # res = []
    # while x:
    #     x, i = divmod(x, 10)
    #     res.append(i)
    # return not [i for i in range(len(res) // 2 + 1) if res[i] != res[-1 - i]]

    return True if x >= 0 and str(x) == str(x)[::-1] else False


print(is_palindrome(121))
print(is_palindrome(1221))
print(is_palindrome(-121))
print(is_palindrome(10))
print(is_palindrome(0))
# True
# True
# False
# False
# True