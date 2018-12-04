def judgeSquareSum(c):
    """
    :type c: int
    :rtype: bool
    """
    i = 0
    temp = int(c ** 0.5)
    while i < temp:
        num = i ** 2 + temp ** 2
        if num > c:
            temp -= 1
        elif num < c:
            i += 1
        else:
            print(i, temp)
            return True
    return False


print(judgeSquareSum(5))
print(judgeSquareSum(3))

# True
# False